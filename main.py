import canvasapi
import openai
import sys
import smtplib, ssl,email

port = 465  # For SSL
password = "P@8687"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("nathandai03222@gmail.com", "ndai0322")

url = "https://canvas.stgeorges.bc.ca/"

key = "4970~3cQXu5Tkblz37E6EyCNEsG567XEjdIuIoNjGp5f4XBpjb0MFRN7UCI3odogj1fBh"

openai.api_key = "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"


g = open("gpt.txt","a")
f = open("done.txt","a")
l = open("done.txt")
p = open("gpt.txt")

canvas = canvasapi.Canvas(url,key)

user = canvas.get_user("self")

model_engine = "text-davinci-003"




courses = canvas.get_courses(enrollment_state = "active")

"""
prompt = "<p>In Chapter 4 of the Outsiders, the Soc's push Ponyboy underwater and he loses consciousness, and when he wakes up, Johnny is covered in blood and Bob is dead. However, there is a major (intentional) gap in the narrative here. Because we are reading this story from Ponyboy's point of view, we don't know what happens when he loses consciousness. We also don't know what other characters are thinking, like Randy, Bob, or Johnny.</p> <p>In this assignment, you will re-write this section of the novel from another character's point of view. You should focus on the time between Ponyboy being pushed underwater and Ponyboy waking up, though you can start a little bit before if you need to add a bit of context. This is a very short span of time, probably less than two minutes in real time, so focus on the details and don't give me pages of backstory and brand new events.</p><p>First, pick a character you want to focus on. Johnny? Bob? Randy? Another Soc? A bystander we don't see in the novel?&nbsp;</p><p>Then, think about who that person is. What is their personality? Age? Education level? What kinds of things are they interested in? What kind of music do they like? What would their vocabulary be like? What kind of references would they use when making comparisons? It might be helpful to do some research pop culture on America in the early 60's.</p><p>You will be focusing on creating a <strong>consistent voice and point of view</strong>, and <strong>showing, not telling</strong>.</p><p>Your composition should be 500-750 words, double spaced, with a title. You <strong>must work on the Google Doc that I provide</strong>, and you must work on this <strong>in class only</strong>.</p><script ></script>How long should this take?"


completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        )
response = completion.choices[0].text
print(response)
"""



for course in courses:
    try: 
        assignments = course.get_assignments(order_by = "due_at",bucket = "upcoming")

        for assignment in assignments:
            temp =assignment.description


            if temp not in l.read():
                f.write(temp)
            
        
                #print('<div class="description user_content">' in temp)
                prompt = temp + "How long should this take?"
                print(prompt)
                completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
            )

                response = completion.choices[0].text
                print(response)

                s = assignment.name + " due at: " + assignment.due_at + " " + response + "\n"
                

                g.write(s)
            

    
        
       
    except:continue 




sender_email = "chipotlehelper@gmail.com"
receiver_email = input("please enter  your email adress")
server.sendmail(sender_email, receiver_email, "hi")