import whisper
from whisper.utils import get_writer

agent = whisper.load_model("base")
arquivo="ccs_150926_pt2"
caminho = f"./src/audios/{arquivo}.m4a"

response = agent.transcribe(
  caminho,
  fp16=False,
  initial_prompt="""
  Escreva de forma legível, bem pontuado e usando quebras de linhas.
  Faça duas quebras de linhas a cada ponto final.
  Toda transcrição desse ser feita em português brasileiro""")

with open(f"./src/outputs/{arquivo}.txt", "w", encoding="utf-8") as f:
  f.write(response["text"])

print("Transcrição concluída")
