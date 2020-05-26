import smtplib


class mail_me:

    def __init__(self, username, password, sent_to, message):
        self.username = username
        self.password = password
        self.sent_to = sent_to
        self.message = message

    def email(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.username, self.password)
        server.sendmail(self.username, self.sent_to, self.message)
        server.quit()


if __name__ == "__main__":
    username = input("Username:")
    password = input("Password:")
    to = input("Sent to:")
    message = input("Write your message:")
    mail = mail_me(username, password, sent_to, message)
    mail.email()
