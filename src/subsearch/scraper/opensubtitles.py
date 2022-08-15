from data import __video_directory__
from utils import log

from . import opensubtitles_soup


# decides what to do with all the scrape data
def scrape(param, lang: str, hi: str) -> list | None:
    """
    Scrape opensubtitles for subtitles using the given parameters.

    Args:
        param (_type_): url_opensubtitles, file_hash
        lang (str): desired language
        hi (str): if hearing impaired subtitles are desired

    Returns:
        list | None: download links for the subtitle
    """
    to_be_downloaded = opensubtitles_soup.search_for_hash(param.url_opensubtitles, lang, hi)
    if to_be_downloaded is None:
        if param.tv_series:
            log.output(f"No TV-series found matching hash {param.file_hash}")
        else:
            log.output(f"No movies found matching hash {param.file_hash}")
        return None

    download_info: list = []
    log.output(f"Preparing  hash {param.file_hash} for download")
    for current_num, (dl_url) in enumerate(to_be_downloaded):
        total_num = len(to_be_downloaded)
        current_num += 1
        file_path = f"{__video_directory__}\\opensubtitles_{current_num}.zip"
        current_num = (file_path, dl_url, current_num, total_num)
        download_info.append(current_num)
    log.output(f"Done with tasks")
    return download_info
