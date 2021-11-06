import vk_api
from vk_api.audio import VkAudio
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

VK_GROUP_ID = os.getenv('VK_GROUP_ID')
VK_LOGIN = os.getenv('VK_LOGIN')
VK_PASSWORD = os.getenv('VK_PASSWORD')

vk_session = vk_api.VkApi(VK_LOGIN, VK_PASSWORD)
vk_session.auth()

vk = vk_session.get_api()

vk_audio = VkAudio(vk_session, convert_m3u8_links=True)
tracks = vk_audio.get_iter()

vk_message = ''

delta = timedelta(days=1)
vk_publish_date = (datetime.now() + delta).timestamp()

vk_photo_attach = 'photo' + VK_GROUP_ID + '_' + '456239108'

track = next(tracks)

vk_audio_attach = 'audio' + str(track['owner_id']) + '_' + str(track['id'])

vk_attachments = vk_audio_attach + ',' + vk_photo_attach
print(vk.wall.post(message=vk_message, owner_id=VK_GROUP_ID, attachments=vk_attachments, publish_date=vk_publish_date))
