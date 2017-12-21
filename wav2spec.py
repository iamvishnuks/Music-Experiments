from pydub import AudioSegment
from pydub.utils import make_chunks
import glob
import os
waves=glob.glob('*.wav')
pat=os.getcwd()

#Listing all files

for i in waves:
    path=pat+'/'+i
    w=i
    print path
    myaudio = AudioSegment.from_file(path , "wav")
    chunk_length_ms = 10000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
    #Export all of the individual chunks as wav files
    for i, chunk in enumerate(chunks):
        chunk_name = w.split('.')[0]+"chunk{0}.wav".format(i)
        print chunk_name
        print "exporting", chunk_name
        chunk.export(chunk_name, format="wav")


#Generate spectrographs

from scipy.io import wavfile
import glob
import os
waves=glob.glob('*.wav')
pat=os.getcwd()

def graph_spectrogram(wav_file):
    rate, data = get_wav_info(wav_file)
    print type(data),len(data)
    nfft = 256  # Length of the windowing segments
    fs = 256    # Sampling frequency
    pxx, freqs, bins, im = plt.specgram(data, nfft,fs)
    print "pxx : ",len(pxx)
    print "freqs : ",len(freqs)
    print "bins : ",len(bins)
    #plt.axis('on')
    #plt.show()
    plt.axis('off')
    plt.savefig(wav_file.split('.')[0]+'.png',
                dpi=100, # Dots per inch
                frameon='false',
                aspect='normal',
                bbox_inches='tight',
                pad_inches=0) # Spectrogram saved as a .png

def get_wav_info(wav_file):
    rate, data = wavfile.read(wav_file)
    return rate, data

for f in waves:
    try:
        pat=os.getcwd()
        wav_file = pat+'/'+f # Filename of the wav file
        graph_spectrogram(wav_file)
    except Exception as e:
        print "error",e
