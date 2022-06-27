class youtubeScrape():
    
    
    
    def init(self):
        
        pass

    def scrape_comments_with_replies(self):
        
        global df
        
        import import_ipynb

        api_key = "AIzaSyDCRyhMHavZXmkkQdCTGg5JPohZYyBxyRc"

        from apiclient.discovery import build

        youtube = build("youtube", "v3", developerKey = api_key)

        import pandas as pd


        ID = "JMUxmLyrhSk"

        box = [["Name", "Comment", "Time", "Likes", "Reply Count"]]



        data = youtube.commentThreads().list(part = "snippet", videoId = ID, maxResults = "100", textFormat = "plainText").execute()

        for i in data["items"]:

            name = i["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]

            comment = i["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

            published_at = i["snippet"]["topLevelComment"]["snippet"]["publishedAt"]

            likes = i["snippet"]["topLevelComment"]["snippet"]["likeCount"]

            replies = i["snippet"]["totalReplyCount"]

            box.append([name, comment, published_at, likes, replies])

            totalReplyCount = i["snippet"]["totalReplyCount"]


            if totalReplyCount > 0:

                parent = i["snippet"]["topLevelComment"]["id"]

                data2 = youtube.comments().list(part = "snippet", maxResults = "100", parentId = parent, textFormat = "plainText").execute()


                for i in data2["items"]:


                    name = i["snippet"]["authorDisplayName"]

                    comment = i["snippet"]["textDisplay"]

                    published_at = i["snippet"]["publishedAt"]

                    likes = i["snippet"]["likeCount"]

                    replies = ""

                    box.append([name, comment, published_at, likes, replies])


        while ("nextPageToken" in data):

            data = youtube.commentThreads().list(part = "snippet", videoId = ID, pageToken = data["nextPageToken"], maxResults = "100", textFormat = "plainText").execute()

            for i in data["items"]:

                name = i["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]

                comment = i["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

                published_at = i["snippet"]["topLevelComment"]["snippet"]["publishedAt"]

                likes = i["snippet"]["topLevelComment"]["snippet"]["likeCount"]

                replies = i["snippet"]["totalReplyCount"]

                box.append([name, comment, published_at, likes, replies])

                totalReplyCount = i["snippet"]["totalReplyCount"]


                if totalReplyCount > 0:

                    parent = i["snippet"]["topLevelComment"]["id"]

                    data2 = youtube.comments().list(part = "snippet", maxResults = "100", parentId = parent, textFormat = "plainText").execute()


                    for i in data2["items"]:


                        name = i["snippet"]["authorDisplayName"]

                        comment = i["snippet"]["textDisplay"]

                        published_at = i["snippet"]["publishedAt"]

                        likes = i["snippet"]["likeCount"]

                        replies = ""

                        box.append([name, comment, published_at, likes, replies])        



        df = pd.DataFrame({"Name" : [i[0] for i in box], "Comment" : [i[1] for i in box], "Time" : [i[2] for i in box],

                     "Likes" : [i[3] for i in box], "Reply Count" : [i[4] for i in box]})


        df.to_csv("youtube_comment.csv", index = False, header = False)

        return "Sucessfull! Check the CSV file that you have just created."
    
        #return df
    
        #self.fetchingComments()

    
    
    
    def fetchingComments(self):
        
        import pandas as pd
        
        #scrape_comments_with_replies(self)
        
        #for lett in df:
            
            #lett[1:50]
            
        
        
        #scrape_comments_with_replies(self)
        
        #yest = fetchingComments(scrape_comments_with_replies(self))
        
        #yest = youtubeScrape.scrape_comments_with_replies(self)
        
        #box = [["Name", "Comment", "Time", "Likes", "Reply Count"]]

        #df = pd.DataFrame({"Name" : [i[0] for i in box], "Comment" : [i[1] for i in box], "Time" : [i[2] for i in box],

                   #      "Likes" : [i[3] for i in box], "Reply Count" : [i[4] for i in box]})


        #df.head()[1:]
        
        yest = df[1:50]
        
        #fetchingComments()
        
        return yest
        
    
    
    
    
    def idLength(self):
        
        import pandas as pd
        
        idLength = len("JMUxmLyrhSk")
        
        return idLength
    
    
    
    def seperateCommentingColumn(self):
        
        import pandas as pd
        
        separateFields = pd.read_csv("youtube_comment.csv")
        
        commentingColumn = separateFields["Comment"]
        
        return commentingColumn
        
    
                
    

