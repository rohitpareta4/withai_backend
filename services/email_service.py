import os
import resend
from core.config import settings

resend.api_key=settings.RESEND_API_KEY
print("API KEY EXISTS:", bool(settings.RESEND_API_KEY))

def send_todo_email(email:str,todos:list[str]):

    print("sending email to -----",email)
    todolist=""

    for x in todos:
        todolist+=f"<li>{x}</li>"

    html_content = f"""
    <h2>You have incomplete Todos</h2>

    <p>Here are the tasks you still need to complete:</p>

    <ul>
        {todolist}
    </ul>

    <p>Keep going! 🚀</p>
    """


    response = resend.Emails.send({
    "from": "WithAI <onboarding@resend.dev>",
    "to": [email],
    "subject": "You have incomplete Todos",
    "html": html_content
})



