# https://github.com/YongHaoWu/NeteaseCloudMusicFlac/blob/61a437e94787b311ae3bb4300430a4fb618e625c/main.py#L169-L195

# download music via ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as executor:
        counter = collections.Counter()
        song_ids = executor.map(get_songid, song_list)
        song_infos = executor.map(get_song_info, song_ids)
        res = [i for i in song_infos if i['data'] == True]
        logger.info("获取歌曲信息完成，开始下载。")
        session = requests.session()
        d = tqdm.tqdm(total=len(res))
        download = partial(download_song, session=session, mp3_option=mp3_option,
                           download_folder=download_folder, display=d, counter=counter)
        executor.map(download, res)


# another example with threading
# run data manipulation 
# https://github.com/huangsam/ultimate-python/blob/ed78cb6a74f2a7912df273093d706131d99675af/ultimatepython/advanced/thread.py#L22-L51

def run_thread_workers(work, data):
    """Run thread workers that invoke work on each data element."""
    results = set()

    # We can use a with statement to ensure workers are cleaned up promptly
    with ThreadPoolExecutor() as executor:
        # Note that results are returned out of order
        work_queue = (executor.submit(work, item) for item in data)
        for future in as_completed(work_queue):
            results.add(future.result())

    return results


def main():
    original_data = {num for num in range(5)}
    expected_data = {(item * 2) for item in original_data}

    # Let's get the data using the simple approach
    simple_start = datetime.now()
    simple_data = {multiply_by_two(item) for item in original_data}
    simple_duration = datetime.now() - simple_start

    # The simple approach has the expected data
    assert simple_data == expected_data

    # Let's get the data using the threaded approach
    thread_start = datetime.now()
    thread_data = run_thread_workers(multiply_by_two, original_data)
    thread_duration = datetime.now() - thread_start
