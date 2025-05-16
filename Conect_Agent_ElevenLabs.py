import os
import sys
import time
import signal
import logging
import threading

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs 
from elevenlabs.conversational_ai.conversation  import Conversation, ConversationConfig
from elevenlabs.conversational_ai.default_audio_interface   import DefaultAudioInterface

load_dotenv()

class Asisten:
    def __init__(self):
        self.api_key            = None
        self.agent_id           = None
        self.client             = None
        self.conversation       = None
        self.id_conversation    = None

    def start(self):
        logging.info(f"**** INICIANDO THREAD ASISTEN ****")
        threading.Thread(target=self.init_asisten, daemon=True).start()

    def init_asisten(self):
        self.api_key    = os.getenv("ELEVENLABS_API_KEY")
        self.agent_id   = os.getenv("AGENT_ID")

        if not self.api_key:
            logging.warning(f"La variable de entorno ELEVENLABS_API_KEY debe ser definida")

        if not self.agent_id:
            logging.warning(f"La variable de entorno AGENT_ID debe ser definida")

        self.client = ElevenLabs(api_key=self.api_key)

        self.conversation = Conversation(
            client                              = self.client,
            agent_id                            = self.agent_id,
            requires_auth                       = bool(self.api_key),
            audio_interface                     = DefaultAudioInterface(),
            callback_agent_response             = self.callback_agent_response,
            callback_agent_response_correction  = self.callback_agent_response_correction,
            callback_user_transcript            = self.callback_user_transcript,
        )
        self.conversation.start_session()

        self.id_conversation  = self.conversation.wait_for_session_end()
        logging.info(f"*"*10)
        logging.info(f"ID OBTENIDO DE LA CONVERSACIÓN: {self.id_conversation}")
        logging.info(f"*"*10)

    def callback_agent_response(self, original):
        logging.info(f"{self.__class__.__name__}: {original}")

    def callback_agent_response_correction(self, original, corrected):
        logging.info(f"{self.__class__.__name__}: {original=} -> {corrected=}")

    def callback_user_transcript(self, transcript):
        logging.info(f"{self.__class__.__name__}: {transcript=}")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    asisten = Asisten()
    asisten.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        logging.info("TERMINANDO APLICACION")