import torch
from tts_webui.utils.manage_model_state import manage_model_state
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from transformers import VitsTokenizer, VitsModel


@manage_model_state("mms")
def preload_models_if_needed(language="eng") -> tuple["VitsModel", "VitsTokenizer"]:
    from transformers import VitsTokenizer, VitsModel

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = VitsModel.from_pretrained(  # type: ignore
        f"facebook/mms-tts-{language}",
    )
    model = model.to(device)  # type: ignore
    tokenizer = VitsTokenizer.from_pretrained(  # type: ignore
        f"facebook/mms-tts-{language}",
    )  # type: ignore
    return model, tokenizer


def tts(
    text,
    language="eng",
    speaking_rate=1.0,
    noise_scale=0.667,
    noise_scale_duration=0.8,
    **kwargs,
):
    model, tokenizer = preload_models_if_needed(language)
    model.speaking_rate = speaking_rate
    model.noise_scale = noise_scale
    model.noise_scale_duration = noise_scale_duration
    inputs = tokenizer(text=text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model(**inputs)  # type: ignore
    waveform = outputs.waveform[0].cpu().numpy().squeeze()
    return {
        "audio_out": (model.config.sampling_rate, waveform),
    }