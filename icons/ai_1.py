"""AI desktop apps, local-LLM runners, AI image tools and agentic code editors."""
import math
from pix import icon

AI = 'dev'


def _bubble(c, x0, y0, x1, y1, col, tail='left', r=4):
    """Speech bubble body + tail."""
    c.rrect(x0, y0, x1, y1, col, r)
    if tail == 'left':
        c.poly([(x0 + 3, y1 - 1), (x0 + 10, y1 - 1), (x0 + 2, y1 + 5)], col)
    else:
        c.poly([(x1 - 10, y1 - 1), (x1 - 3, y1 - 1), (x1 - 1, y1 + 5)], col)


def _cloud(c, col):
    c.circle(11, 17, 7, col)
    c.circle(18, 13, 9, col)
    c.circle(23.5, 18.5, 5.5, col)
    c.rrect(5, 17, 28, 25, col, 3)


# ====================================================================== chat desktops

@icon('chatgpt-desktop', ['chatgpt-desktop-bin', 'ChatGPT', 'chatgpt-app', 'chatgpt-desktop-app'], AI,
      'ChatGPT Desktop')
def chatgpt_desktop(c):
    # the blossom knot, white on a dark disc
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    for k in range(6):
        a = math.radians(k * 60 + 30)
        c.ring(16 + 4.6 * math.cos(a), 16 + 4.6 * math.sin(a), 5.2, 3.4, 'W')
    c.circle(16, 16, 2.2, 'k')
    c.replace('W', 'w', (17, 17, 28, 28))
    c.outline()


@icon('codex', ['openai-codex', 'codex-desktop', 'com.openai.codex', 'codex-cli', 'codex-app'], AI, 'Codex')
def codex(c):
    _cloud(c, 'B')
    c.bevel(['B'])
    c.sprite(10, 15, """
        W....
        WW...
        .WW..
        WW...
        W..WWWW
    """)
    c.outline()


@icon('cherry-studio', ['cherry-studio-bin', 'CherryStudio', 'com.cherry_ai.CherryStudio',
                        'cherry-studio-appimage'], AI, 'Cherry Studio')
def cherry_studio(c):
    c.line(10, 19, 16, 7, '4', 2)
    c.line(21, 20, 17, 7, '4', 2)
    c.poly([(17, 7), (24, 3), (28, 6), (21, 9)], 'G')
    c.line(19, 7, 26, 5, '4')
    c.circle(9, 22.5, 6, 'R')
    c.circle(22, 23, 6, 'R')
    c.bevel(['R', 'G'])
    c.pixels([(7, 20), (8, 19), (20, 20), (21, 19)], 'W')
    c.outline()


@icon('lobehub', ['lobe-chat', 'lobechat', 'LobeHub', 'LobeChat', 'lobehub-desktop', 'lobe-chat-bin'], AI,
      'LobeHub')
def lobehub(c):
    # a squishy smiling blob
    c.ellipse(16, 17.5, 13, 11, 'M')
    c.circle(10, 9, 4, 'M')
    c.circle(22, 9, 4, 'M')
    c.bevel(['M'])
    c.rect(10, 13, 12, 17, 'W'); c.rect(20, 13, 22, 17, 'W')
    c.rect(11, 14, 12, 16, 'K'); c.rect(21, 14, 22, 16, 'K')
    c.hline(13, 19, 22, '7'); c.px(12, 21, '7'); c.px(20, 21, '7')
    c.pixels([(7, 19), (8, 19), (24, 19), (25, 19)], 'P')
    c.outline()


@icon('jan', ['ai.jan.Jan', 'jan-bin', 'Jan', 'jan-appimage', 'jan-ai'], AI, 'Jan')
def jan(c):
    # chunky J hand-drawn hook with a dot
    c.rect(15, 3, 26, 8, 'B')
    c.rect(19, 3, 25, 20, 'B')
    c.arc(15, 19, 10, 4, 0, 180, 'B')
    c.rect(5, 17, 11, 19, 'B')
    c.rect(5, 3, 11, 9, 'Y')
    c.bevel(['B', 'Y'])
    c.outline()


@icon('lm-studio', ['lmstudio', 'lmstudio-bin', 'ai.elementlabs.lmstudio', 'LM-Studio', 'LMStudio', 'lm-studio-bin', 'lm-studio-appimage',
                    'ai.lmstudio.LMStudio'], AI, 'LM Studio')
def lm_studio(c):
    # staggered bars of the LM Studio mark
    bars = [(4, 20, 'M'), (9, 27, 'B'), (6, 23, 'M'), (11, 28, 'B'), (3, 18, 'M')]
    for i, (x0, x1, col) in enumerate(bars):
        c.rrect(x0, 3 + i * 5, x1, 6 + i * 5, col, 1)
    c.bevel(['M', 'B'])
    c.outline()


@icon('ollama', ['ollama-app', 'com.ollama.Ollama', 'ollama-desktop', 'ollama-bin'], AI, 'Ollama')
def ollama(c):
    # front-facing llama head
    c.rrect(8, 3, 12, 12, 'W', 2)
    c.rrect(19, 3, 23, 12, 'W', 2)
    c.rrect(6, 9, 25, 28, 'W', 6)
    c.bevel(['W'])
    c.rect(9, 5, 10, 10, 'w'); c.rect(21, 5, 22, 10, 'w')
    c.rect(10, 15, 11, 17, 'K'); c.rect(20, 15, 21, 17, 'K')
    c.ellipse(16, 22.5, 6, 4, 'w')
    c.rect(14, 21, 17, 22, 'K')
    c.px(15, 23, 'K'); c.px(16, 23, 'K')
    c.outline()


@icon('open-webui', ['openwebui', 'open-webui-desktop', 'OpenWebUI'], AI, 'Open WebUI')
def open_webui(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    c.ring(13, 16, 7, 4, 'W')
    c.rect(21, 9, 24, 22, 'W')
    c.replace('W', 'w', (12, 20, 28, 28))
    c.outline()


@icon('anythingllm-desktop', ['anythingllm', 'anythingllm-desktop-bin', 'AnythingLLMDesktop',
                              'anythingllm-desktop-appimage', 'AnythingLLM'], AI, 'AnythingLLM')
def anythingllm(c):
    # infinity loop
    c.circle(10, 16, 7, 'C')
    c.circle(22, 16, 7, 'C')
    c.bevel(['C'])
    c.circle(10, 16, 3, '.')
    c.circle(22, 16, 3, '.')
    c.rect(15, 14, 16, 17, '5')
    c.outline()


@icon('msty', ['msty-bin', 'Msty', 'msty-app', 'msty-studio', 'msty-appimage'], AI, 'Msty')
def msty(c):
    # rounded lowercase m: three arches
    c.rrect(3, 6, 28, 16, 'M', 5)
    c.rect(3, 12, 8, 27, 'M')
    c.rect(13, 12, 18, 27, 'M')
    c.rect(23, 12, 28, 27, 'M')
    c.bevel(['M'])
    c.outline()


@icon('chatbox', ['xyz.chatboxapp.app', 'chatbox-bin', 'Chatbox', 'chatbox-ce', 'xyz.chatboxapp.ce',
                  'chatbox-appimage'], AI, 'Chatbox')
def chatbox(c):
    _bubble(c, 3, 3, 28, 23, 'B', 'left', 5)
    c.bevel(['B'])
    c.rect(10, 10, 11, 12, 'W'); c.rect(20, 10, 21, 12, 'W')
    c.sprite(10, 15, """
        W..........
        .W........W
        ..WWWWWWWW.
    """)
    c.outline()


@icon('gpt4all', ['io.gpt4all.gpt4all', 'gpt4all-chat', 'gpt4all-bin', 'io.gpt4all.GPT4All', 'GPT4All'], AI,
      'GPT4All')
def gpt4all(c):
    _bubble(c, 3, 3, 28, 23, 'G', 'right', 4)
    c.bevel(['G'])
    c.text(11, 7, '4', 'W', scale=2)
    c.rect(11, 7, 12, 8, 'G')
    c.outline()


@icon('com.jeffser.Alpaca', ['alpaca', 'alpaca-ai', 'Alpaca'], AI, 'Alpaca')
def alpaca(c):
    # fluffy alpaca in profile
    c.rrect(8, 14, 17, 28, 'W', 3)            # fluffy neck
    c.circle(14, 12, 8, 'W')                 # fluffy head
    c.circle(10, 7, 4, 'W')
    c.circle(18, 7, 4, 'W')
    c.rrect(18, 11, 27, 18, 'n', 3)           # muzzle
    c.poly([(7, 5), (9, 3), (11, 7)], 'n')    # ear
    c.bevel(['W', 'n'])
    c.rect(17, 11, 18, 12, 'K')
    c.px(26, 13, 'K')
    c.hline(22, 25, 16, '8')
    for y in (20, 24):
        c.hline(10, 15, y, 'w')
    c.outline()


@icon('io.github.qwersyk.Newelle', ['newelle', 'Newelle'], AI, 'Newelle')
def newelle(c):
    _bubble(c, 3, 4, 28, 23, 'C', 'left', 5)
    c.bevel(['C'])
    # four-point sparkle
    c.poly([(16, 6), (18, 12), (24, 14), (18, 16), (16, 22), (14, 16), (8, 14), (14, 12)], 'W')
    c.px(16, 14, 'c')
    c.outline()


# ====================================================================== image generation

@icon('stable-diffusion-webui', ['sd-webui', 'automatic1111', 'stable-diffusion', 'stable-diffusion-webui-forge',
                                 'sd-webui-forge', 'stable-diffusion-webui-git'], AI, 'Stable Diffusion WebUI')
def sd_webui(c):
    # painting with a magic sparkle
    c.rect(3, 7, 24, 28, 'N')
    c.rect(5, 9, 22, 26, 'b')
    c.poly([(5, 26.5), (11, 16), (16, 22), (19, 19), (22.5, 26.5)], 'G')
    c.circle(10, 13, 2.5, 'Y')
    c.bevel(['N'])
    c.poly([(23, 2), (24.5, 6), (28.5, 7.5), (24.5, 9), (23, 13), (21.5, 9), (17.5, 7.5), (21.5, 6)], 'Y')
    c.outline()


@icon('comfyui', ['ComfyUI', 'comfyui-desktop', 'comfy-ui', 'comfyui-bin', 'comfyui-git'], AI, 'ComfyUI')
def comfyui(c):
    # slanted yellow C on a blue parallelogram
    c.poly([(9, 3), (29, 3), (23, 29), (3, 29)], 'B')
    c.poly([(12, 7), (24, 7), (23, 11), (14.5, 11), (12.5, 21), (21, 21), (20, 25), (8, 25)], 'Y')
    c.bevel(['B', 'Y'])
    c.outline()


@icon('fooocus', ['Fooocus', 'fooocus-git'], AI, 'Fooocus')
def fooocus(c):
    # focus brackets around a sparkle
    for x, y, sx, sy in ((3, 3, 1, 1), (28, 3, -1, 1), (3, 28, 1, -1), (28, 28, -1, -1)):
        c.rect(x, y, x + sx * 7, y + sy * 2, 'O')
        c.rect(x, y, x + sx * 2, y + sy * 7, 'O')
    c.poly([(16, 7), (18, 14), (25, 16), (18, 18), (16, 25), (14, 18), (7, 16), (14, 14)], 'Y')
    c.bevel(['O', 'Y'])
    c.outline()


@icon('invokeai', ['invoke-ai', 'invoke-community-edition', 'InvokeAI', 'invoke', 'invokeai-bin'], AI, 'InvokeAI')
def invokeai(c):
    # dark tile cut by the bright "invoke" wedge
    c.rrect(3, 3, 28, 28, 'k', 3)
    c.bevel(['k'], dark=False)
    c.poly([(8, 8), (24, 8), (24, 12), (13, 12), (24, 23), (21, 24), (8, 11)], 'C')
    c.poly([(8, 20), (12, 24), (8, 24)], 'C')
    c.bevel(['C'], dark=False)
    c.outline()


@icon('chainner', ['chaiNNer', 'chainner-bin', 'chainner-appimage'], AI, 'chaiNNer')
def chainner(c):
    # two chain links of nodes
    c.rrect(3, 8, 17, 17, 'M', 4)
    c.rrect(14, 15, 28, 24, 'B', 4)
    c.bevel(['M', 'B'])
    c.rrect(7, 11, 13, 14, '.', 1)
    c.rrect(18, 18, 24, 21, '.', 1)
    c.outline()


# ====================================================================== speech

@icon('io.github.chidiwilliams.Buzz', ['buzz', 'buzz-captions', 'buzz-bin', 'Buzz'], AI, 'Buzz')
def buzz(c):
    _bubble(c, 3, 4, 28, 23, 'Y', 'left', 5)
    c.bevel(['Y'])
    for i, h in enumerate([3, 7, 11, 6, 9, 4]):
        x = 8 + i * 3
        c.rect(x, 13 - h // 2, x + 1, 13 + h // 2, 'k')
    c.outline()


@icon('net.mkiol.SpeechNote', ['dsnote', 'speechnote', 'speech-note', 'SpeechNote'], AI, 'Speech Note')
def speechnote(c):
    c.rect(4, 3, 21, 28, 'W')
    c.shade_below(['W'], 'w')
    for i in range(6):
        c.hline(7, 18, 7 + i * 3, 'S')
    # microphone
    c.rrect(19, 9, 26, 21, 'R', 3)
    c.bevel(['R'])
    c.hline(21, 24, 13, '1'); c.hline(21, 24, 16, '1')
    c.rect(22, 22, 23, 25, 's')
    c.rect(19, 26, 26, 27, 's')
    c.outline()


# ====================================================================== agentic editors

@icon('windsurf', ['windsurf-bin', 'Windsurf', 'codeium-windsurf', 'windsurf-next', 'com.exafunction.windsurf',
                   'windsurf-next-bin'], AI, 'Windsurf')
def windsurf(c):
    # a sail over a curling wave
    c.poly([(17, 2), (27, 19), (17, 19)], 'W')
    c.poly([(15, 5), (15, 19), (6, 19)], 'w')
    c.vline(16, 2, 21, 'S')
    c.poly([(3, 22), (10, 19), (20, 20), (28, 18), (27, 24), (19, 28), (4, 28)], 'C')
    c.bevel(['C'])
    c.hline(6, 18, 24, '5')
    c.outline()


@icon('trae', ['trae-bin', 'Trae', 'trae-cn', 'trae-ide', 'trae-appimage'], AI, 'Trae')
def trae(c):
    # notched frame with two diamond eyes
    c.rect(3, 6, 28, 26, 'G')
    c.tri((3, 6), (9, 6), (3, 12), '.')
    c.rect(7, 10, 24, 22, '.')
    c.bevel(['G'])
    for x in (12, 19):
        c.poly([(x, 13), (x + 2, 15.5), (x, 18), (x - 2, 15.5)], 'G')
    c.outline()


@icon('kiro', ['kiro-bin', 'Kiro', 'kiro-ide', 'dev.kiro.Kiro', 'kiro-appimage'], AI, 'Kiro')
def kiro(c):
    # chubby purple ghost
    c.circle(16, 13, 10, 'M')
    c.rect(6, 13, 25, 24, 'M')
    for x in (6, 13, 20):
        c.rrect(x, 23, x + 5, 28, 'M', 2)
    c.bevel(['M'])
    c.ellipse(12.5, 13, 2, 3, 'W')
    c.ellipse(19.5, 13, 2, 3, 'W')
    c.pixels([(12, 13), (19, 13), (12, 14), (19, 14)], 'K')
    c.outline()


@icon('void', ['void-editor', 'void-bin', 'Void', 'voideditor', 'com.voideditor.Void', 'void-editor-bin'], AI,
      'Void')
def void(c):
    # black hole with an accretion disc
    c.circle(16, 16, 10, 'M')
    c.circle(16, 16, 8, 'K')
    c.ellipse(16, 17, 13, 4, 'O')
    c.ellipse(16, 17, 8.5, 1.8, 'K')
    c.rect(9, 12, 22, 16, 'K')
    c.bevel(['O', 'M'])
    c.outline()


@icon('pearai', ['PearAI', 'pearai-bin', 'pearai-app', 'pearai-appimage'], AI, 'PearAI')
def pearai(c):
    c.circle(16, 20, 8, 'G')
    c.circle(16, 12, 5, 'G')
    c.poly([(11, 13), (21, 13), (23.5, 19), (8.5, 19)], 'G')
    c.rect(15, 4, 16, 7, 'N')
    c.poly([(17, 6), (24, 3), (26, 5), (19, 8)], 'g')
    c.bevel(['G'])
    c.pixels([(12, 17), (11, 18), (11, 19)], 'g')
    c.outline()


def _tui(c, chrome='S', screen='k'):
    """Small terminal window used by CLI agents: chrome bar + dark screen."""
    c.rrect(3, 5, 28, 26, chrome, 2)
    c.bevel([chrome])
    c.rect(5, 9, 26, 24, screen)
    c.pixels([(5, 7), (7, 7), (9, 7)], 'W')


@icon('aider', ['aider-chat', 'aider-ai', 'aider-install'], AI, 'aider')
def aider(c):
    _tui(c, 'G')
    c.sprite(7, 12, """
        G....
        GG...
        .GG..
        GG...
        G....
    """)
    c.text(14, 12, 'AI', 'g', font=3)
    c.hline(7, 18, 20, '4'); c.hline(7, 13, 22, '4')
    c.outline()


@icon('opencode', ['opencode-bin', 'opencode-ai', 'opencode-desktop', 'sst-opencode', 'opencode-cli'], AI,
      'opencode')
def opencode(c):
    # stacked open square frames of the opencode mark
    c.rect(5, 3, 26, 28, 'w')
    c.rect(9, 7, 22, 24, 'K')
    c.rect(9, 15, 22, 24, 's')
    c.bevel(['w'])
    c.outline()


@icon('gemini-cli', ['google-gemini-cli', 'gemini-cli-bin'], AI, 'Gemini CLI')
def gemini_cli(c):
    _tui(c, 'B')
    c.sprite(7, 12, """
        b....
        .b...
        ..b..
        .b...
        b....
    """)
    c.poly([(19, 10), (20.5, 15), (25.5, 16.5), (20.5, 18), (19, 23), (17.5, 18), (12.5, 16.5), (17.5, 15)], 'M')
    c.px(19, 14, 'm'); c.px(19, 15, 'm')
    c.outline()


@icon('continue-dev', ['continue', 'continuedev', 'Continue'], AI, 'Continue')
def continue_dev(c):
    for x0, col in ((3, 'S'), (14, 'W')):
        c.poly([(x0, 3), (x0 + 6, 3), (x0 + 15, 16), (x0 + 6, 29), (x0, 29), (x0 + 9, 16)], col)
    c.bevel(['S', 'W'])
    c.outline()


@icon('cline', ['cline-cli', 'cline-bot', 'Cline'], AI, 'Cline')
def cline(c):
    # friendly robot head
    c.rect(15, 3, 16, 5, 's')
    c.rect(13, 2, 18, 3, 'S')
    c.rrect(5, 6, 26, 27, 'w', 6)
    c.rect(3, 13, 5, 19, 'S'); c.rect(26, 13, 28, 19, 'S')
    c.bevel(['w'])
    c.rrect(8, 11, 23, 22, 'k', 3)
    c.ellipse(12.5, 16.5, 1.6, 2.6, 'C')
    c.ellipse(19.5, 16.5, 1.6, 2.6, 'C')
    c.outline()


@icon('goose', ['goose-desktop', 'Goose', 'block-goose', 'goose-bin', 'io.github.block.Goose', 'goose-cli'], AI,
      'Goose')
def goose(c):
    c.circle(14, 8.5, 5.5, 'W')
    c.rect(10, 9, 17, 20, 'W')
    c.ellipse(15, 23, 11, 6, 'W')
    c.poly([(18, 6), (28, 9), (18, 12)], 'O')
    c.bevel(['W', 'O'])
    c.rect(14, 6, 15, 7, 'K')
    c.hline(10, 22, 24, 'w'); c.hline(13, 24, 26, 'w')
    c.outline()


@icon('mistral', ['le-chat', 'mistral-le-chat', 'mistral-webapp', 'lechat', 'mistral-ai', 'chat.mistral.ai',
                  'mistral-desktop'], AI, 'Mistral Le Chat')
def mistral(c):
    # the blocky M, banded yellow -> red
    m = ["X...X", "XX.XX", "XXXXX", "X.X.X", "X...X"]
    cols = ['Y', 'y', 'O', '2', 'R']
    for j, row in enumerate(m):
        for i, ch in enumerate(row):
            if ch == 'X':
                c.rect(4 + i * 5, 4 + j * 5, 8 + i * 5, 8 + j * 5, cols[j])
    c.outline()


@icon('grok', ['grok-webapp', 'grok-desktop', 'xai-grok', 'grok.com', 'grok-bin'], AI, 'Grok')
def grok(c):
    c.circle(16, 16, 13, 'k')
    c.bevel(['k'], dark=False)
    c.arc(16, 16, 9, 6.5, 100, 350, 'W')
    c.line(7, 25, 25, 7, 'W', 2)
    c.rect(18, 12, 19, 13, 'k')
    c.outline()


@icon('poe', ['poe-webapp', 'poe-desktop', 'com.quora.poe', 'poe.com', 'poe-bin'], AI, 'Poe')
def poe(c):
    _bubble(c, 3, 4, 28, 22, 'M', 'right', 5)
    c.bevel(['M'])
    c.rrect(8, 9, 23, 17, 'm', 3)
    c.rect(11, 12, 12, 14, '7'); c.rect(19, 12, 20, 14, '7')
    c.outline()


@icon('huggingface', ['hugging-face', 'huggingface-webapp', 'huggingface.co', 'huggingface-desktop'], AI,
      'Hugging Face')
def huggingface(c):
    c.circle(16, 14.5, 11.5, 'Y')
    c.bevel(['Y'])
    c.rect(10, 9, 11, 11, 'K'); c.rect(20, 9, 21, 11, 'K')
    c.ellipse(16, 17.5, 5, 3, 'K')
    c.rect(11, 15, 20, 16, 'Y')
    c.hline(14, 17, 19, 'R')
    # hugging hands
    c.rrect(3, 20, 10, 27, 'O', 2)
    c.rrect(21, 20, 28, 27, 'O', 2)
    c.bevel(['O'])
    c.outline()


@icon('qwen', ['tongyi-qianwen', 'com.alibaba.tongyi', 'qwen-chat', 'qwen-webapp', 'chat.qwen.ai', 'tongyi', 'qwen-desktop'], AI, 'Qwen')
def qwen(c):
    # hexagonal knot: hex ring with a twisted gap
    pts = [(16 + 13 * math.cos(math.radians(a)), 16 + 13 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    c.poly(pts, 'M')
    inner = [(16 + 7 * math.cos(math.radians(a)), 16 + 7 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
    c.poly(inner, '.')
    c.bevel(['M'])
    c.poly([(16, 9), (22, 12.5), (22, 15.5), (16, 12)], 'm')
    c.poly([(16, 16), (20, 18.5), (16, 21), (12, 18.5)], 'W')
    c.outline()


@icon('kimi', ['kimi-webapp', 'kimi-desktop', 'moonshot-kimi', 'kimi.ai', 'kimi-cli'], AI, 'Kimi')
def kimi(c):
    c.rrect(3, 3, 28, 28, 'k', 5)
    c.bevel(['k'], dark=False)
    c.rect(8, 8, 11, 23, 'W')
    c.poly([(11, 15), (18, 8), (22, 8), (14, 16), (22, 23.5), (18, 23.5), (11, 17)], 'W')
    c.circle(22.5, 9.5, 2.5, 'B')
    c.outline()


@icon('meta-ai', ['meta-ai-webapp', 'meta.ai', 'meta-ai-desktop'], AI, 'Meta AI')
def meta_ai(c):
    c.circle(16, 16, 13, 'B')
    c.circle(16, 16, 8, 'M')
    c.circle(16, 16, 5, '.')
    c.bevel(['B', 'M'])
    c.outline()


@icon('sillytavern', ['SillyTavern', 'silly-tavern', 'sillytavern-launcher'], AI, 'SillyTavern')
def sillytavern(c):
    # foaming tavern mug
    c.ring(22, 17.5, 6.5, 3.5, 'N')
    c.rect(5, 9, 21, 28, 'N')
    c.bevel(['N'])
    for x in (9, 13, 17):
        c.vline(x, 12, 25, '8')
    c.circle(8, 8, 3.5, 'W'); c.circle(13, 7, 4, 'W'); c.circle(18.5, 8, 3.5, 'W')
    c.rect(5, 8, 21, 10, 'W')
    c.hline(5, 21, 10, 'w')
    c.outline()


@icon('notebooklm', ['notebooklm-webapp', 'google-notebooklm', 'notebooklm.google.com'], AI, 'NotebookLM')
def notebooklm(c):
    # stacked arches of the NotebookLM mark
    c.arc(16, 20, 12.5, 9, 180, 360, 'w')
    c.arc(16, 20, 7.5, 4, 180, 360, 'w')
    c.rect(4, 20, 6, 27, 'w'); c.rect(25, 20, 27, 27, 'w')
    c.rect(9, 20, 11, 27, 'w'); c.rect(20, 20, 22, 27, 'w')
    c.bevel(['w'])
    c.outline()


@icon('pinokio', ['pinokio-bin', 'Pinokio', 'computer.pinokio', 'pinokio-appimage'], AI, 'Pinokio')
def pinokio(c):
    # wooden puppet head with a long nose
    c.circle(13, 16, 10, 'n')
    c.rect(19, 13, 28, 16, 'N')
    c.poly([(4, 8), (13, 2), (22, 8)], 'R')
    c.rect(3, 7, 23, 9, 'R')
    c.bevel(['n', 'N', 'R'])
    c.rect(13, 11, 14, 13, 'K')
    c.hline(10, 15, 20, '8')
    c.px(9, 19, '8')
    c.outline()


@icon('koboldcpp', ['koboldcpp-bin', 'kobold-cpp', 'koboldai', 'KoboldCpp', 'koboldcpp-cuda'], AI, 'KoboldCpp')
def koboldcpp(c):
    # little horned kobold dragon head
    c.poly([(7, 9), (4, 2), (11, 7)], 'y')
    c.poly([(19, 7), (24, 1), (24, 9)], 'y')
    c.rrect(5, 7, 24, 22, 'G', 5)
    c.rrect(14, 15, 28, 25, 'G', 3)
    c.bevel(['G', 'y'])
    c.rect(10, 11, 12, 13, 'Y'); c.px(11, 12, 'K')
    c.pixels([(24, 18), (26, 18)], '4')
    c.hline(16, 27, 22, '4')
    c.outline()


@icon('localai', ['local-ai', 'LocalAI', 'localai-bin'], AI, 'LocalAI')
def localai(c):
    # house-shaped chip: AI that stays home
    c.poly([(16, 3), (29, 13), (3, 13)], 'R')
    c.rect(6, 12, 26, 28, 'w')
    c.bevel(['R', 'w'])
    c.rect(11, 16, 21, 25, 'k')
    for y in (17, 20, 23):
        c.hline(9, 10, y, 's'); c.hline(22, 23, y, 's')
    c.text(13, 18, 'AI', 'G', font=3, gap=0) if False else c.text(12, 18, 'AI', 'G', font=3)
    c.outline()


@icon('crush', ['charm-crush', 'crush-bin', 'crush-cli'], AI, 'Crush')
def crush(c):
    # Charm's heart-shaped crush
    c.circle(10, 11, 7, 'P')
    c.circle(22, 11, 7, 'P')
    c.poly([(3, 13), (29, 13), (16, 28)], 'P')
    c.bevel(['P'])
    c.sprite(9, 11, """
        W.....
        .W....
        ..W...
        .W....
        W..WWW
    """, {'W': 'W'})
    c.outline()


@icon('text-generation-webui', ['oobabooga', 'textgen-webui', 'text-generation-webui-git'], AI,
      'Text Generation WebUI')
def textgen(c):
    # browser window with a typing cursor
    c.rrect(3, 4, 28, 27, 'S', 2)
    c.rect(3, 4, 28, 8, 'O')
    c.bevel(['S', 'O'])
    c.rect(5, 10, 26, 25, 'W')
    for i, w in enumerate([16, 12, 18, 8]):
        c.hline(7, 7 + w, 12 + i * 3, 'S')
    c.rect(16, 21, 17, 24, 'O')
    c.outline()


@icon('character-ai', ['characterai', 'character.ai', 'character-ai-webapp'], AI, 'Character.AI')
def character_ai(c):
    # theatre mask face in a bubble
    _bubble(c, 3, 3, 28, 22, 'k', 'left', 6)
    c.bevel(['k'], dark=False)
    c.text(7, 9, 'C', 'W'); c.px(13, 15, 'W')
    c.text(15, 9, 'AI', 'W', font=3)
    c.outline()
