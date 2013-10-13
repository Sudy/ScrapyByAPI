# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#-*- coding=utf-8 -*-
import csv
from csv import DictWriter
from datetime import datetime
class ScrapyweibobyapiPipeline(object):
    def __init__(self):
        self.followerCsv = csv.writer(open("follower.csv", "a"),
                   delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        self.statusCsv = csv.writer(open("status.csv", "a"),
           delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        self.commentCsv = csv.writer(open("comment.csv", "a"),
           delimiter='\t', quoting=csv.QUOTE_MINIMAL)

        self.obj_dict = {1:self.followerCsv,
        			2:self.statusCsv,
        			3:self.commentCsv
        }
    def process_item(self, item, spider):
    	result_list = []
    	for key in item.keys():
    		if key != "tid":
    			if isinstance(item[key],unicode):
    				result_list.append(unicode(item[key],"utf-8"))
    			else:
    				result_list.append(item[key])
    	return result_list
    	#self.obj_dict[item["tid"]].writerow(result_list)
