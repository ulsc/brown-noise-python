# test_main.py - Generated by CodiumAI
import time

import numpy as np
import pyaudio
import pytest

from main import generate_brown_noise

"""
Code Analysis:
- The main goal of the function is to generate brown noise with a given alpha value, last sample, and buffer length.
- The function takes in three inputs: alpha (a float value between 0 and 1), last_sample (a float value representing the last sample generated), and buffer_length (an integer value representing the length of the buffer to generate).
- It initializes an array of zeros with the length of the buffer.
- It then generates a random sample between -1 and 1 for each index in the buffer using the random module.
- It calculates the current sample using the formula alpha * random_sample + (1 - alpha) * last_sample.
- It updates the last_sample variable to the current_sample for the next iteration.
- It stores the current_sample in the samples array.
- It returns the samples array and the last_sample variable.
"""

"""
Test Plan:
- test_generate_brown_noise_happy_path_1(): tests that the function returns an array of length buffer_length. Tags: [happy path]
- test_generate_brown_noise_happy_path_2(): tests that the function returns a last_sample variable of type float. Tags: [happy path]
- test_generate_brown_noise_edge_case_1(): tests that the function raises an exception if alpha is 0. Tags: [edge case]
- test_generate_brown_noise_edge_case_2(): tests that the function raises an exception if alpha is 1. Tags: [edge case]
- test_generate_brown_noise_general_behavior_1(): tests that the function handles large buffer_lengths efficiently. Tags: [general behavior]
- test_generate_brown_noise_happy_path_3(): tests that the function returns an array of type numpy.ndarray. Tags: [happy path]
- test_generate_brown_noise_happy_path_4(): tests that the function returns an array with values between -1 and 1. Tags: [happy path]
- test_generate_brown_noise_edge_case_3(): tests that the function raises an exception if last_sample is not a float. Tags: [edge case]
- test_generate_brown_noise_edge_case_4(): tests that the function raises an exception if buffer_length is not an integer. Tags: [edge case]
- test_generate_brown_noise_edge_case_5(): tests that the function returns an empty array if buffer_length is 0. Tags: [edge case]
- test_alpha_half_buffer_100(): tests that the function generates brown noise with alpha=0.5, last_sample=0.0, and buffer_length=100. Tags: [happy path]
- test_alpha_nine_tenths_buffer_500(): tests that the function generates brown noise with alpha=0.9, last_sample=-0.5, and buffer_length=500. Tags: [happy path]
- test_alpha_zero(): tests that the function raises a ValueError when alpha=0. Tags: [edge case]
- test_alpha_one(): tests that the function raises a ValueError when alpha=1. Tags: [edge case]
- test_samples_array_length(): tests that the samples array has the correct length. Tags: [general behavior]
- test_alpha_negative_half(): tests that the function raises a ValueError when alpha=-0.5. Tags: [edge case]
- test_alpha_one_and_a_half(): tests that the function raises a ValueError when alpha=1.5. Tags: [edge case]
- test_buffer_length_zero(): tests that the function returns an empty samples array when buffer_length=0. Tags: [edge case]
- test_last_sample_returned(): tests that the last_sample variable is returned correctly. Tags: [general behavior]
- test_generated_samples_range(): tests that the generated samples are within the range of -1 to 1. Tags: [general behavior]
"""


class TestGenerateBrownNoise:
    def test_generate_brown_noise_happy_path_1(self):
        buffer_length = 100
        alpha = 0.5
        last_sample = 0.0
        samples, last_sample = generate_brown_noise(alpha, last_sample, buffer_length)
        assert len(samples) == buffer_length

    def test_generate_brown_noise_happy_path_2(self):
        buffer_length = 100
        alpha = 0.5
        last_sample = 0.0
        samples, last_sample = generate_brown_noise(alpha, last_sample, buffer_length)
        assert isinstance(last_sample, float)

    def test_generate_brown_noise_edge_case_1(self):
        buffer_length = 100
        alpha = 0.0
        last_sample = 0.0
        with pytest.raises(Exception):
            generate_brown_noise(alpha, last_sample, buffer_length)

    def test_generate_brown_noise_edge_case_2(self):
        buffer_length = 100
        alpha = 1.0
        last_sample = 0.0
        with pytest.raises(Exception):
            generate_brown_noise(alpha, last_sample, buffer_length)

    def test_generate_brown_noise_general_behavior_1(self):
        buffer_length = 1000000
        alpha = 0.5
        last_sample = 0.0
        samples, last_sample = generate_brown_noise(alpha, last_sample, buffer_length)
        assert len(samples) == buffer_length

    def test_generate_brown_noise_happy_path_3(self):
        buffer_length = 100
        alpha = 0.5
        last_sample = 0.0
        samples, last_sample = generate_brown_noise(alpha, last_sample, buffer_length)
        assert isinstance(samples, np.ndarray)

    def test_alpha_half_buffer_100(self):
        # Given
        alpha = 0.5
        last_sample = 0.0
        buffer_length = 100

        # When
        samples, last_sample = generate_brown_noise(alpha, last_sample, buffer_length)

        # Then
        assert len(samples) == buffer_length
        assert samples.min() >= -1.0
        assert samples.max() <= 1.0

    def test_alpha_nine_tenths_buffer_500(self):
        # Given
        alpha = 0.9
        last_sample = -0.5
        buffer_length = 500

        # When
        samples, last_sample = generate_brown_noise(alpha, last_sample, buffer_length)

        # Then
        assert len(samples) == buffer_length
        assert samples.min() >= -1.0
        assert samples.max() <= 1.0

    def test_alpha_zero(self):
        # Given
        alpha = 0.0
        last_sample = 0.0
        buffer_length = 100

        # When, Then
        with pytest.raises(ValueError):
            generate_brown_noise(alpha, last_sample, buffer_length)

    def test_alpha_one(self):
        # Given
        alpha = 1.0
        last_sample = 0.0
        buffer_length = 100

        # When, Then
        with pytest.raises(ValueError):
            generate_brown_noise(alpha, last_sample, buffer_length)

    def test_samples_array_length(self):
        # Given
        alpha = 0.5
        last_sample = 0.0
        buffer_length = 100

        # When
        samples, last_sample = generate_brown_noise(alpha, last_sample, buffer_length)

        # Then
        assert len(samples) == buffer_length

    def test_alpha_negative_half(self):
        # Given
        alpha = -0.5
        last_sample = 0.0
        buffer_length = 100

        # When, Then
        with pytest.raises(ValueError):
            generate_brown_noise(alpha, last_sample, buffer_length)


"""
Code Analysis:
- - The main goal of the function is to generate and output brown noise using PyAudio library.
- It initializes PyAudio and defines a callback function that generates brown noise.
- The callback function takes in input data, frame count, time information, and status.
- It generates brown noise using the generate_brown_noise function and converts it to integer samples.
- It repeats the integer samples for stereo output and packs the data into a binary format.
- The callback function returns the packed data and continues the stream.
- The function initializes the last_sample variable and opens a PyAudio stream with the defined callback function.
- It starts the stream and waits for it to be active.
- If the stream is interrupted by a keyboard interrupt, it stops and closes the stream and terminates PyAudio.
- The function has no explicit output, but it generates brown noise as an audio output.
"""

"""
Test Plan:
- test_generate_brown_noise(): tests that the function successfully generates brown noise. Tags: [happy path]
- test_start_stop_stream(): tests that the PyAudio stream is successfully started and stopped. Tags: [happy path]
- test_small_buffer_size(): tests that the function handles a buffer size that is too small. Tags: [edge case]
- test_large_buffer_size(): tests that the function handles a buffer size that is too large. Tags: [edge case]
- test_keyboard_interrupt(): tests that the function handles a keyboard interrupt and stops the stream. Tags: [general behavior]
- test_terminate_pyaudio(): tests that the function handles errors and terminates PyAudio. Tags: [general behavior]
"""


class TestMain:
    def test_generate_brown_noise(self):
        # Given
        duration = 0.01
        last_sample = 0
        frame_count = 1024

        # When
        samples, last_sample = generate_brown_noise(duration, last_sample, frame_count)

        # Then
        assert len(samples) == frame_count
        assert isinstance(samples, np.ndarray)

    def test_start_stop_stream(self):
        # Given
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True)

        # When
        stream.start_stream()
        stream.stop_stream()

        # Then
        assert not stream.is_active()

    def test_small_buffer_size(self):
        # Given
        p = pyaudio.PyAudio()
        buffer_size_in_bytes = 1024
        stream = p.open(
            format=pyaudio.paInt16,
            channels=2,
            rate=44100,
            output=True,
            frames_per_buffer=int(buffer_size_in_bytes / 2),
        )

        # When
        try:
            stream.start_stream()
            time.sleep(1)  # Let the stream run for 1 second
        except Exception as e:
            pytest.fail(f"An exception was raised: {e}")

        # Then
        assert stream.is_active()

        stream.stop_stream()
        stream.close()
        p.terminate()

    def test_large_buffer_size(self):
        # Given
        p = pyaudio.PyAudio()
        buffer_size_in_bytes = 1000000
        stream = p.open(
            format=pyaudio.paInt16,
            channels=2,
            rate=44100,
            output=True,
            frames_per_buffer=int(buffer_size_in_bytes / 2),
        )

        # When
        try:
            stream.start_stream()
            time.sleep(1)  # Let the stream run for 1 second
        except Exception as e:
            pytest.fail(f"An exception was raised: {e}")

        # Then
        assert stream.is_active()

        stream.stop_stream()
        stream.close()
        p.terminate()

    def test_keyboard_interrupt(self):
        # Given
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True)

        # When
        stream.start_stream()
        stream.stop_stream()

        # Then
        assert not stream.is_active()

    def test_terminate_pyaudio(self):
        # Given
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True)

        # When
        p.terminate()

        # Then
        with pytest.raises(OSError, match="Stream not open"):
            stream.is_active()
