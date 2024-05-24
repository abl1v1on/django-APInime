from anime_site.celery import app

from .utils import call_in_new_anime_episodes


@app.task
def send_mail_task(subject, message, recipient_list, html_template, context=None):
    call_in_new_anime_episodes(
        subject,
        message,
        recipient_list,
        html_template,
        context
    )
