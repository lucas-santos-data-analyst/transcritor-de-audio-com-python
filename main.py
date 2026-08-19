import whisper
from whisper.utils import get_writer

agent = whisper.load_model("base")

response = agent.transcribe(
  "./src/audios/aula-ccs-agentes-inteligentes.m4a", 
  fp16=False)

with open("./src/outputs/transcrição.txt", "w", encoding="utf-8") as f:
  f.write(response["text"])

print("Transcrição concluída")