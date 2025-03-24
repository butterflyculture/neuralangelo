import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime
import pytz

class NeoVoxelBot():
    def __init__(self, channel):
        '''
        init
        '''
        # Get the directory where this script is located
        current_dir = Path(__file__).parent
        env_path = current_dir / '.env'
        # Load env:
        load_dotenv(env_path)

        # Establish client:
        self.client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
        self.channel = channel
    
    def __get_ist_time(self):
        '''
        Get current time in IST
        '''
        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist)
        return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    def send_message(self, msg):
        '''
        Send message with IST timestamp prefix
        ''' 
        msg = f'[{self.__get_ist_time()}]: '+ msg
        return self.client.chat_postMessage(channel=self.channel, text=msg)

if __name__=="__main__":
    # Debug code:
    bot = NeoVoxelBot(channel='neovoxel-bot')
    bot.send_message("Hey, testing")