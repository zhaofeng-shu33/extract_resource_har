# Introduction
  Media stream serving is very popular. But in some cases such as playing video on meeting, the advertisement is annoying. Or the network condition is undetermined. Therefore, we need to download the video to a local file. We can watch it using Chrome browser and save all
  requests and response information in a `har` format.
  It is indeed a json format and the video and images in it are encoded with base64. As a result, I write a Python script to extract all the `ts` files and save
  them under the current directory. Using `ffmpeg` or other tools, we can concatenate these `ts` files to produce an mp4 file.