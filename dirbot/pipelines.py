from scrapy.exceptions import DropItem
import json
from data_manage import engine,Content
from sqlalchemy.orm import sessionmaker
from scrapy.pipelines.images import ImagesPipeline
import re,os,datetime,urllib

class StoreInMysql(object):

    def store_img(self,url,path='download/imgs/'):
        _url_name = re.match(r'http.*/(.*)\.(\w+)$',url)
        # today = datetime.date.isoformat(datetime.date.today())
        store_path = path + _url_name.groups()[0] + '.' + _url_name.groups()[1]
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.exists(store_path):
            return store_path
        else:
            f = file(store_path,'wb')
            conn = urllib.urlopen(url)
            f.write(conn.read())
            f.close()
            return store_path


    def process_item(self, item, spider):
        SessionCls = sessionmaker(bind=engine)
        session = SessionCls()
        contents = Content()
        # for i in item:
        _title = item['title'][0].encode('utf8')

        if contents.get_content(_title):
            pass
        else:
            contents.title = _title
            contents.abstract = item['abstract'][0].encode('utf8')
            contents.ptime = item['ptime'][0].encode('utf8')
            contents.content = item['content'].encode('utf8')
            contents.img_url = self.store_img(item['image_urls'][0])
            session.add(contents)
            session.commit()
        # print item



