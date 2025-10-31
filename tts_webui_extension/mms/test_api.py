from api import tts


def test_tts():
    """Smoke test for the tts function."""
    result = tts("Hello world", language="eng")
    assert "audio_out" in result
    assert isinstance(result["audio_out"], tuple)
    assert len(result["audio_out"]) == 2
    sampling_rate, waveform = result["audio_out"]
    assert isinstance(sampling_rate, int)
    assert hasattr(waveform, '__len__')  # Check if waveform is array-like
    print("Smoke test passed!")


if __name__ == "__main__":
    test_tts()