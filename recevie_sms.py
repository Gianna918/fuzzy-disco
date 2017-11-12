from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import random 
app = Flask(__name__)

@app.route("/sms", methods=['GET','POST'])
def incoming_sms():
    body = request.values.get('Body', None )
    resp = MessagingResponse()
    lst1 = ["sad","unhappy","depressed","dissapointed","embarassed"]
    lst2 = ["happy","excited","joyful","cheerful","glad","ecstatic", "calm"]
    lst3 = ["scared","frightened","afraid","terrified","petrified"]
    lst4 = ["stressed","overwhelmed","nervous","confused"]
    lst5 = ["lonely","dejected","isolated"]
    lst6 = ["mad","angry"]
    lst7 = ["sleepy","tired","bored",""]
    lst_ans = ["done1", "done2","done3","done4", "done5"]
    correct_ans = ["first aid", "nothing", "history","i understand","maid"]
    body = body.lower()
    body = body.strip()
    if body in lst2:
        if random.randint(0,1)==0:  
            msg = resp.message("What a wonderful phrase!")
            msg.media("https://i1.wp.com/heisenbergreport.com/wp-content/uploads/2017/06/hakuna.png?fit=634%2C363&ssl=1")
        else:
            msg = resp.message("Always smile!")
            msg.media("https://images-na.ssl-images-amazon.com/images/I/81IXBCQbTFL._SX355_.jpg")

    elif body in lst3:
        if random.randint(0,1) == 0:
            msg = resp.message("Be Strong!")
            msg.media("https://i.pinimg.com/736x/ed/91/fc/ed91fc88684313500c520ab6c1a81091--sad-disney-quotes-motivational-disney-quotes.jpg")
        else:
            msg = resp.message("Don't give up!")
            msg.media("https://i.pinimg.com/736x/b9/10/0a/b9100ab2fe6cb05c241d5c5f5b18ae32.jpg")
    elif body in lst5:
        if random.randint(0,1)==0:
            msg = resp.message("You're not alone!")
            msg.media("https://pbs.twimg.com/media/BpJZsndCcAAwf7Z.jpg")
        else:
            msg = resp.message("We have all been there, just plow through it! It gets better!")
            msg.media("http://emilysquotes.com/wp-content/uploads/2015/07/Remember-the-time-you-feel-lonely-is-the-time-you-most-need-to-be-by-yourself.-Life%E2%80%99s-cruelest-irony..jpg")
    elif body in lst1:
        if random.randint(0,1) ==0:
            msg = resp.message("Listen to music, go out for a walk, and/or binge watch a show! Make it a YOU day!")
            msg.media("http://bridgesofhope.com.ph/wp-content/uploads/positive-coping-mechanisms.jpg")
        else: 
            msg = resp.message("Don't feel sad get glad.")
            msg.media("https://i.pinimg.com/736x/a6/33/55/a63355bfafe4841f5909276d0cffc819--funny-inspirational-quotes-cute-text-quotes.jpg")
    elif body in lst4:
        if random.randint(0,1)==1:
            msg = resp.message("Calm down and take it slow and steady")
            msg.media("https://i.pinimg.com/originals/af/8b/99/af8b99269855eca4ff0e9ca7eda39afb.jpg")
        else:
            msg = resp.message("Be organized and manage your time wisely")
            msg.media("http://cdn2.bigcommerce.com/server2100/da4a7/products/489/images/119/Keep-Calm-and-Carry-On-Navy-Blue-Poster-Front__69597.1319984235.1280.1280.jpg?c=2")
    elif body in lst6:
        if random.randint(0,1)==0:
            msg = resp.message()
            msg.media("https://i.pinimg.com/736x/40/4e/75/404e75940404ebc91d45eff64415f3f5--anger-quotes-quotes-positive.jpg")
        else:
            msg = resp.message()
            msg.media("https://i.pinimg.com/736x/dd/71/b7/dd71b7aa20313f9d86846d597e7e1bfe--anger-quotes-control-quotes-anger.jpg")
        
    elif body in lst7:
        y = 4
        if random.randint(0,y)==0:
            msg = resp.message("Please input answer (no special symbols requires and make sure word is spelled correctly): \n If you give up type done1")
            msg.media("http://brainden.com/images/aid-rebus-puzzle.gif")
        elif random.randint(0,y) == 1:
            msg = resp.message("Please input answer (no special symbols requires and make sure word is spelled correctly): \n If you give up type done2")
            msg = resp.message("It is greater than God and more evil than the devil. The poor have it, the rich need it and if you eat it you’ll die. What is it?")

        elif random.randint(0,y) == 2:
            msg = resp.message("Please input answer (no special symbols requires and make sure word is spelled correctly): \n If you give up type done3")
            msg = resp.message("You will always find me in the past. I can be created in the present, But the future can never taint me. What am I?")
        elif random.randint(0,y) == 3:
            msg = resp.message("Please input answer (no special symbols requires and make sure word is spelled correctly): \n If you give up type done4")
            msg.media("https://3.bp.blogspot.com/-Ek0IAiZ3zTk/VZgWAswOlSI/AAAAAAAAOL0/HHSQLvB3nCk/s320/Rebus.png")
        else:
            msg = resp.message("Please input answer (no special symbols requires and make sure word is spelled correctly and is one word): \n If you give up type done5")
            msg = resp.message("A man is found dead on a Sunday morning. His wife calls the police immediately. The police question the wife and staff. The wife said she was asleep, the cook said he was cooking breakfast, the gardener said she was picking vegetables, the butler said he was cleaning the closet, and the maid said she was getting the post. The police immediately arrested the murderer.Who was the murderer?")
        
    elif body in correct_ans:
        msg = resp.message("Correct")
        msg = resp.message("Type 'bored' (no apostraphes) for another puzzle. Note: puzzles might be repeated.")
        

    elif body in lst_ans:
        if lst_ans[0] == body:
            msg = resp.message("first aid")
        elif lst_ans[1] == body:
            msg = resp.message("nothing")
        elif lst_ans[2] == body:
            msg = resp.message("history")
        elif lst_ans[3] == body:
            msg = resp.message("i understand")
        else:
            msg = resp.message("maid")
        msg = resp.message("Type 'bored' (no apostraphes) for another puzzle. Note: puzzles might be repeated.")



    elif body == "whacky":
        msg = resp.message("You are a hacker, who creates, makes, and changes the future. Whackathon is only the first step")
        msg.media("https://pbs.twimg.com/profile_images/910334412558127105/ySrQZtZT.jpg")    
    else:
        x=3
        if random.randint(0,x) == 0:
            msg = resp.message("Yassss")
            msg.media("https://i.imgur.com/Yp1Wglo.jpg")
        elif random.randint(0,x) == 1:
            msg = resp.message("I'm just like my country, I'm young, scrappy, and hungry!")
            msg.media("http://photosaws.sparkpeople.com/guid/43beed56-ed2d-4734-bd07-304d24c0e675.PNG")
        elif random.randint(0,x) == 2:
            msg = resp.message("No one knows")
            msg.media("http://www.enzasbargains.com/wp-content/uploads/2016/11/Moana-Quote.jpg")
        else:
            msg = resp.message("Unlucky!")
        msg = resp.message("try another word choice")
    print(body)
    return str(resp)
    
if __name__ == "__main__":
    app.run(debug = True)


