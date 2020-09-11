# thumbnail_maker.py
import time
import os
import logging

from threading import Thread
from queue import Queue
from urllib.parse import urlparse
from urllib.request import urlretrieve

import PIL
from PIL import Image

filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logfile.log')

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename=filename, level=logging.DEBUG, format=FORMAT)


class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_queue = Queue()
        self.dl_queue = Queue()

    def download_image(self):
        while not self.dl_queue.empty():
            # last item
            try:
                url = self.dl_queue.get(block=False)
                # download each image and save to the input dir
                img_filename = urlparse(url).path.split('/')[-1]
                dest_path = self.input_dir + os.path.sep + img_filename
                urlretrieve(url, dest_path)
                self.img_queue.put(img_filename)
                self.dl_queue.task_done()
            except Queue.empty:
                logging.info("Queue empty")
            
    # def download_images(self, img_url_list):
    #     # validate inputs
    #     if not img_url_list:
    #         return
    #     os.makedirs(self.input_dir, exist_ok=True)
        
    #     logging.info("beginning image downloads")

    #     start = time.perf_counter()
    #     for url in img_url_list:
    #         logging.info("download image at URL " + url)
    #         img_filename = urlparse(url).path.split('/')[-1]
    #         dest_path = self.input_dir + os.path.sep + img_filename
    #         urlretrieve(url, dest_path)
    #         self.img_queue.put(img_filename)
    #     end = time.perf_counter()
        
    #     self.img_queue.put(None) # marks no more item
    #     logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self):
        logging.info("beginning image resizing")
        target_sizes = [32, 64, 200]
        num_images = len(os.listdir(self.input_dir))

        start = time.perf_counter()
        while True:
            filename = self.img_queue.get()
            if not filename:
                # empty file means done with the image downloading, i.e. no more items from the queue
                self.img_queue.task_done()
                break
            logging.info("resizing image {}".format(filename))
            orig_img = Image.open(self.input_dir + os.path.sep + filename)
            for basewidth in target_sizes:
                img = orig_img
                # calculate target height of the resized image to maintain the aspect ratio
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                # perform resizing
                img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)
                
                # save the resized image to the output dir with a modified file name 
                new_filename = os.path.splitext(filename)[0] + \
                    '_' + str(basewidth) + os.path.splitext(filename)[1]
                img.save(self.output_dir + os.path.sep + new_filename)

            os.remove(self.input_dir + os.path.sep + filename)
            logging.info("done resizing image {}".format(filename))
            self.img_queue.task_done()
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(num_images, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        start = time.perf_counter()

        # loading all download urls into the download queue
        for img_url in img_url_list:
            self.dl_queue.put(img_url)

        num_dl_threads = 4 

        for _ in range(num_dl_threads):
            t = Thread(target=self.download_image)
            t.start()
        
        t2 = Thread(target=self.perform_resizing)

        t2.start()

        # block main thread until all downloads complete
        self.dl_queue.join()
        # put poison pill
        self.img_queue.put(None) 
        t2.join()

        end = time.perf_counter()
        logging.info("END make_thumbnails in {} seconds".format(end - start))

if __name__ == '__main__':
    IMG_URLS = \
    ['https://dl.dropboxusercontent.com/s/2fu69d8lfesbhru/pexels-photo-48603.jpeg',
     'https://dl.dropboxusercontent.com/s/zch88m6sb8a7bm1/pexels-photo-134392.jpeg',
     'https://dl.dropboxusercontent.com/s/lsr6dxw5m2ep5qt/pexels-photo-135130.jpeg',
     'https://dl.dropboxusercontent.com/s/6xinfm0lcnbirb9/pexels-photo-167300.jpeg',
     'https://dl.dropboxusercontent.com/s/2dp2hli32h9p0y6/pexels-photo-167921.jpeg',
     'https://dl.dropboxusercontent.com/s/fjb1m3grcrceqo2/pexels-photo-173125.jpeg',
     'https://dl.dropboxusercontent.com/s/56u8p4oplagc4bp/pexels-photo-185934.jpeg',
     'https://dl.dropboxusercontent.com/s/2s1x7wz4sdvxssr/pexels-photo-192454.jpeg',
     'https://dl.dropboxusercontent.com/s/1gjphqnllzm10hh/pexels-photo-193038.jpeg',
     'https://dl.dropboxusercontent.com/s/pcjz40c8pxpy057/pexels-photo-193043.jpeg',
     'https://dl.dropboxusercontent.com/s/hokdfk7y8zmwe96/pexels-photo-207962.jpeg',
     'https://dl.dropboxusercontent.com/s/k2tk2co7r18juy7/pexels-photo-247917.jpeg',
     'https://dl.dropboxusercontent.com/s/m4xjekvqk4rksbx/pexels-photo-247932.jpeg',
     'https://dl.dropboxusercontent.com/s/znmswtwhcdbpc10/pexels-photo-265186.jpeg',
     'https://dl.dropboxusercontent.com/s/jgb6n4esquhh4gu/pexels-photo-302899.jpeg',
     'https://dl.dropboxusercontent.com/s/rjuggi2ubc1b3bk/pexels-photo-317156.jpeg',
     'https://dl.dropboxusercontent.com/s/cpaog2nwplilrz9/pexels-photo-317383.jpeg',
     'https://dl.dropboxusercontent.com/s/16x2b6ruk18gji5/pexels-photo-320007.jpeg',
     'https://dl.dropboxusercontent.com/s/xqzqzjkcwl52en0/pexels-photo-322207.jpeg',
     'https://dl.dropboxusercontent.com/s/frclthpd7t8exma/pexels-photo-323503.jpeg',
     'https://dl.dropboxusercontent.com/s/7ixez07vnc3jeyg/pexels-photo-324030.jpeg',
     'https://dl.dropboxusercontent.com/s/1xlgrfy861nyhox/pexels-photo-324655.jpeg',
     'https://dl.dropboxusercontent.com/s/v1b03d940lop05d/pexels-photo-324658.jpeg',
     'https://dl.dropboxusercontent.com/s/ehrm5clkucbhvi4/pexels-photo-325520.jpeg',
     'https://dl.dropboxusercontent.com/s/l7ga4ea98hfl49b/pexels-photo-333529.jpeg',
     'https://dl.dropboxusercontent.com/s/rleff9tx000k19j/pexels-photo-341520.jpeg'
    ]
    
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
