import random
import struct

import numpy as np
import pyaudio

sample_rate = 44100
channels = 2
bit_depth = pyaudio.paInt16
bit_depth_in_bytes = 2
bytes_per_sample = channels * bit_depth_in_bytes
buffer_size_in_bytes = sample_rate * bytes_per_sample


def generate_brown_noise(alpha, last_sample, buffer_length):
    if alpha <= 0.0 or alpha >= 1.0:
        raise ValueError("Alpha must be between 0 and 1, exclusive.")

    samples = np.zeros(buffer_length)

    for i in range(buffer_length):
        random_sample = 2 * random.random() - 1
        current_sample = alpha * random_sample + (1 - alpha) * last_sample
        last_sample = current_sample
        samples[i] = current_sample

    return samples, last_sample


def create_pyaudio_instance():
    return pyaudio.PyAudio()


def create_audio_stream(p, callback, buffer_size):
    stream = p.open(
        format=bit_depth,
        channels=channels,
        rate=sample_rate,
        output=True,
        stream_callback=callback,
        frames_per_buffer=int(buffer_size / 2),
    )
    return stream


def brown_noise_callback(last_sample):
    def callback(in_data, frame_count, time_info, status):
        nonlocal last_sample
        samples, last_sample = generate_brown_noise(0.01, last_sample, frame_count)
        int_samples = np.int16(samples * 32767)
        stereo_samples = np.repeat(int_samples, 2)
        data = struct.pack("<" + "h" * len(stereo_samples), *stereo_samples)
        return data, pyaudio.paContinue

    return callback


def main():
    p = create_pyaudio_instance()
    last_sample = 0
    callback = brown_noise_callback(last_sample)
    stream = create_audio_stream(p, callback, buffer_size_in_bytes)
    stream.start_stream()

    try:
        while stream.is_active():
            pass
    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    main()
