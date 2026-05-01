import os


def _make_tts_fn():
    def tts_fn(
        model: str, text: str, voice: str | None, speed: float | None, params: dict
    ) -> dict:
        from tts_webui_extension.mms.api import tts

        return tts(
            text=text,
            language=params.get("language", "eng"),
            speaking_rate=speed,
            noise_scale=params.get("noise_scale", 0.667),
            noise_scale_duration=params.get("noise_scale_duration", 0.8),
            **params,
        )

    return tts_fn


def register():
    try:
        if os.environ.get("OPENAI_PROXY_HOST"):
            register_unsafe_outprocess()
        else:
            register_unsafe_inprocess()
    except Exception as e:
        print(f"Error registering MMS API adapter: {e}")
        print("MMS TTS will not be available on the OpenAI API.")


def register_unsafe_inprocess():
    from tts_webui_extension.openai_tts_api.services.tts_adapter_registry import (
        register_tts_adapter,
    )

    register_tts_adapter("mms", _make_tts_fn())


def register_unsafe_outprocess():
    from tts_webui_extension.openai_tts_api.harness import setup_oai_server

    setup_oai_server(
        tts_fn=_make_tts_fn(),
        get_voices_fn=lambda model: [],
        model="mms",
    )