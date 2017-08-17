Answer: No. There is no single library/solution in python to do video/audio recording simultaneously. You have to implement both separately and merge the audio and video signal in a smart way to end up with a video/audio file.

I got a solution for the problem you present. My code addresses your three issues:

.- Records video + audio from webcam and microphone simultaneously. .- It saves the final video/audio file as .AVI .- Un-commenting lines 76, 77 and 78 will make the video to be displayed to screen while recording.

My solution uses pyaudio for audio recording, opencv for video recording, and ffmpeg for muxing the two signals. To be able to record both simultaneously, I use multithreading. One thread records video, and a second one the audio. I have uploaded my code to github and also have included all the essential parts it here.

https://github.com/JRodrigoF/AVrecordeR

Note: opencv is not able to control the fps at which the webcamera does the recording. It is only able to specify in the encoding of the file the desired final fps, but the webcamera usually behaves differently according to specifications and light conditions (I found). So the fps have to be controlled at the level of the code.