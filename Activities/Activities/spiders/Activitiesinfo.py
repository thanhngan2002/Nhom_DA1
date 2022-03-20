import scrapy
from ..items import ActivitiesItem

class ActivitiesinfoSpider(scrapy.Spider):
    name = 'Activitiesinfo'
    allowed_domains = ['tripadvisor.com.vn']
    start_urls = ['https://www.tripadvisor.com.vn/Attraction_Review-g293926-d6941969-Reviews-Tu_Hieu_Pagoda-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d4333898-Reviews-Tu_Dam_Pagoda-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d451125-Reviews-The_Noon_Gate_Cua_Ngo_Mon-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d12898868-Reviews-Nguyen_Dinh_Chieu_Walking_Street-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d11680443-Reviews-Luc_Bo_Culture_Space-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d5895985-Reviews-Cat_Tuong_Quan_Zen_House-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d15632400-Reviews-Abandoned_Water_Park-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d6106529-Reviews-Huyen_Tran_Princess_Temple-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d10818173-Reviews-Huyen_Khong_Son_Thuong_Pagoda-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d600402-Reviews-Nine_Dynastic_Urns-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d451118-Reviews-The_Flag_Tower-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d6224999-Reviews-Tiger_Arena-Hue_Thua_Thien_Hue_Province.html',
                  'https://www.tripadvisor.com.vn/Attraction_Review-g293926-d14758714-Reviews-Nha_Vuon_Xuan_Dai-Hue_Thua_Thien_Hue_Province.html']

    def parse(self, response):
        P_name = response.xpath('//h1[@class="WlYyy cPsXC GeSzT"]/text()').get()
        try:
            P_rank = response.xpath('//div[@class="WlYyy diXIH dDKKM"]/text()').get()
        except:
            P_rank = 0
        try:
            P_type = response.xpath('//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div/div/span/section[1]/div/div/span/div/div[1]/div[3]/div/text()').get()
        except:
            P_type = 0
        P_status = response.xpath('//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div/div/span/section[1]/div/div/span/div/div[2]/div[1]/div/div/button/span/text()').get()
        try:
            P_time = response.xpath('//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div/div/span/section[1]/div/div/span/div/div[2]/div[1]/div/div/span/text()').get()
        except:
            P_time = 0
        try:
            P_images = response.xpath('//*[@id="lithium-root"]/main/div[1]/div[2]/div[2]/div/div/span/section[2]/div/div/div/div[2]/span/div/div[1]/div/div/div/div[1]/div/div[7]/button/span/span/text()[2]').get()
        except:
            P_images = 0
        try:
            P_url = response.url
        except:
            P_url = 0
        try:
            P_rate = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[1]/div[1]/text()').get()
            P_rate = float(P_rate)
        except:
            P_rate = 0
        try:
            Total_reviewers = response.xpath('//span[@class="WlYyy diXIH bGusc dDKKM"]/text()').get()
            Total_reviewers = Total_reviewers.replace(' đánh giá','')
            Total_reviewers = Total_reviewers.replace('.','')
            Total_reviewers = int(Total_reviewers)
        except:
            Total_reviewers = 0
        try:
            R_5points = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[2]/div/div[1]/div[2]/div/div[2]/div/text()').get()
            R_5points = int(R_5points)
        except:
            R_5points = 0
        try:
            R_4points = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[2]/div/div[2]/div[2]/div/div[2]/div/text()').get()
            R_4points = int(R_4points)
        except:
            R_4points = 0
        try:
            R_3points = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[2]/div/div[3]/div[2]/div/div[2]/div/text()').get()
            R_3points = int(R_3points)
        except:
            R_3points = 0
        try:
            R_2points = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[2]/div/div[4]/div[2]/div/div[2]/div/text()').get()
            R_2points = int(R_2points)
        except:
            R_2points = 0
        try:
            R_1points = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[3]/span/div/div[2]/div/div[5]/div[2]/div/div/div/text()').get()
            R_1points = int(R_1points)
        except:
            R_1points = 0
        try:
            R_name = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[2]/span/div/div[1]/div[1]/div[2]/span/a/text()').get()
        except:
            R_name = 0
        try: 
            R_address = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[3]/span/div/div[1]/div[1]/div[2]/div/div/span[1]/text()').get()
        except:
            R_address = 0
        try:
            R_idea = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[2]/span/div/div[3]/a/span/text()').get()
        except:
            R_idea = 0
        try:
            R_content = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[2]/span/div/div[4]/text()').get()
        except:
            R_content = 0
        try:
            Time_who = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[4]/span/div/div[5]/div[1]/div/span/text()').get()
        except:
            Time_who = 0
        try:
            R_time = response.xpath('//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[8]/span/div/div[8]/div[2]/text()').get()
        except:
            R_time = 0

        item = ActivitiesItem()
        item['P_name'] = P_name
        item['P_rank'] = P_rank
        item['P_type'] = P_type
        item['P_status'] = P_status
        item['P_time'] = P_time
        item['P_images'] = P_images
        item['P_url'] = P_url
        item['P_rate'] = P_rate
        item['Total_reviewers'] = Total_reviewers
        item['R_5points'] = R_5points
        item['R_4points'] = R_4points
        item['R_3points'] = R_3points
        item['R_2points'] = R_2points
        item['R_1points'] = R_1points
        item['R_name'] = R_name
        item['R_address'] = R_address
        item['R_idea'] = R_idea
        item['R_content'] = R_content
        item['Time_who'] = Time_who
        item['R_time'] = R_time
        yield item
        pass
