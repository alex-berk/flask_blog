import os
import secrets
from flaskblog import app
from PIL import Image

def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/profile_pics/', picture_fn)
	
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn

def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password reset request', sender='a.berk14@yandex.ru', recipients=[user.email])
	msg.body = f'''To reset your password, click here {url_for('users.reset_token', token=token, _external=True)}
If you didn't made any requests, just ignore this mail'''
	mail.send(msg)
