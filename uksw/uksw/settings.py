# -*- coding: utf-8 -*-

# Scrapy settings for uksw project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
import os
from os.path import dirname

path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'uksw'

SPIDER_MODULES = ['uksw.spiders']
NEWSPIDER_MODULE = 'uksw.spiders'


DOWNLOADER_MIDDLEWARES = {
    'misc.middleware.CustomHttpProxyMiddleware': 400,
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

LOG_LEVEL = 'INFO' # DEBUG Minimum level to log. Available levels are: CRITICAL, ERROR, WARNING, INFO, DEBUG. For more info see Logging.
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'uksw.log'
LOG_STDOUT = False # If True, all standard output (and error) of your process will be redirected to the log. For example if you print 'hello' it will appear in the Scrapy log.



CONCURRENT_ITEMS = 100 # Maximum number of concurrent items (per response) to process in parallel in the Item Processor (also known as the Item Pipeline).
CONCURRENT_REQUESTS = 16 # The maximum number of concurrent (ie. simultaneous) requests that will be performed by the Scrapy downloader.
CONCURRENT_REQUESTS_PER_DOMAIN = 8 # The maximum number of concurrent (ie. simultaneous) requests that will be performed to any single domain.
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}
DEPTH_LIMIT = 0 # The maximum depth that will be allowed to crawl for any site. If zero, no limit will be imposed.
DNSCACHE_ENABLED = True # Whether to enable DNS in-memory cache.
DOWNLOADER_MIDDLEWARES = {} # A dict containing the downloader middlewares enabled in your project, and their orders. For more info see Activating a downloader middleware.
DOWNLOADER_STATS = True # Whether to enable downloader stats collection.
DOWNLOAD_DELAY = 0 # The amount of time (in secs) that the downloader should wait before downloading consecutive pages from the same website. This can be used to throttle the crawling speed to avoid hitting servers too hard. Decimal numbers are supported.
# DOWNLOAD_DELAY = 0.25    # 250 ms of delay
#  By default, Scrapy doesn’t wait a fixed amount of time between requests, but uses a random interval between 0.5 and 1.5 * DOWNLOAD_DELAY.
DOWNLOAD_TIMEOUT = 180 # The amount of time (in secs) that the downloader will wait before timing out.
DUPEFILTER_DEBUG = False # By default, RFPDupeFilter only logs the first duplicate request. Setting DUPEFILTER_DEBUG to True will make it log all duplicate requests.
ITEM_PIPELINES = {'uksw.uksw.pipelines.EcolexPipeline'} #A dict containing the item pipelines to use, and their orders. The dict is empty by default order values are arbitrary but it’s customary to define them in the 0-1000 range.
# ITEM_PIPELINES = {
#     'mybot.pipelines.validate.ValidateMyItem': 300,
#     'mybot.pipelines.validate.StoreMyItem': 800,
# }
MEMDEBUG_ENABLED = False # Whether to enable memory debugging.
MEMDEBUG_NOTIFY = [] # When memory debugging is enabled a memory report will be sent to the specified addresses if this setting is not empty, otherwise the report will be written to the log.
# MEMDEBUG_NOTIFY = ['user@example.com']
MEMUSAGE_ENABLED = False # Whether to enable the memory usage extension that will shutdown the Scrapy process when it exceeds a memory limit, and also notify by email when that happened.
MEMUSAGE_LIMIT_MB = 0 # The maximum amount of memory to allow (in megabytes) before shutting down Scrapy (if MEMUSAGE_ENABLED is True). If zero, no check will be performed.
MEMUSAGE_NOTIFY_MAIL = False # MEMUSAGE_NOTIFY_MAIL = ['user@example.com']
MEMUSAGE_REPORT = False # Whether to send a memory usage report after each spider has been closed.
MEMUSAGE_WARNING_MB = 0 # The maximum amount of memory to allow (in megabytes) before sending a warning email notifying about it. If zero, no warning will be produced.
RANDOMIZE_DOWNLOAD_DELAY = True # If enabled, Scrapy will wait a random amount of time (between 0.5 and 1.5 * DOWNLOAD_DELAY) while fetching requests from the same website.
# This randomization decreases the chance of the crawler being detected (and subsequently blocked) by sites which analyze requests looking for statistically significant similarities in the time between their requests.
REDIRECT_MAX_TIMES = 20 # Defines the maximum times a request can be redirected. After this maximum the request’s response is returned as is.
METAREFRESH_MAX_DELAY = 100 # Some sites use meta-refresh for redirecting to a session expired page, so we restrict automatic redirection to a maximum delay (in seconds)
ROBOTSTXT_OBEY = False # If enabled, Scrapy will respect robots.txt policies. For more information see RobotsTxtMiddleware, scrapy.contrib.downloadermiddleware.robotstxt
SCHEDULER = 'scrapy.core.scheduler.Scheduler' # The scheduler to use for crawling.
SPIDER_CONTRACTS = {} # A dict containing the scrapy contracts enabled in your project, used for testing spiders. For more info see Spiders Contracts.
SPIDER_MODULES = [] # A list of modules where Scrapy will look for spiders. SPIDER_MODULES = ['mybot.spiders_prod', 'mybot.spiders_dev']
STATS_CLASS = 'scrapy.statscol.MemoryStatsCollector' # The class to use for collecting stats, who must implement the Stats Collector API.
STATS_DUMP = True # Dump the Scrapy stats (to the Scrapy log) once the spider finishes.
URLLENGTH_LIMIT = 2083 # The maximum URL length to allow for crawled URLs. For more information about the default value for this setting see: http://www.boutell.com/newfaq/misc/urllength.html
USER_AGENT = "Scrapy/VERSION (+http://scrapy.org)" # The default User-Agent to use when crawling, unless overridden.

