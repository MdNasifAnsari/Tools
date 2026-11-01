# Install required package via terminal: --"pip install withoutbg"--


from withoutbg import WithoutBG

abc = WithoutBG.opensource()
wbg = abc.remove_background("./images.png")
wbg.save("./output.png")