#!/usr/bin/env python3
"""Render original, deterministic, independently mixable demo stems; no external samples."""
import json, math, os, wave
import numpy as np
SR=22050
BPM=76
ARRANGEMENTS=[
 ('soft-evening','Soft Evening Jazz','soft','jazz',76,['Cmaj9','Am9','Dm9','G13','Em9','A7b9','Dm9','Cmaj9'],[48,45,50,43,52,45,50,48]),
 ('blues','12-Bar Blues','blues','blues',92,['C7','F7','C7','C7','F7','F7','C7','A7','Dm7','G7','C7','G7'],[48,53,48,48,53,53,48,45,50,43,48,43]),
 ('circle','Circle of Fifths','circle','jazz',82,['Am7','Am7','Am7','Am7','Dm7','G7','Cmaj7','Fmaj7','Bm7b5','E7','Am7'],[45,45,45,45,50,43,48,53,47,52,45]),
 ('bossa-evening','Evening Bossa','soft','bossa',108,['Cmaj9','Am9','Dm9','G13','Em9','A7b9','Dm9','Cmaj9'],[48,45,50,43,52,45,50,48])]
CHORDS=ARRANGEMENTS[0][5]
ROOTS=ARRANGEMENTS[0][6]
BAR=240/BPM
N=round(len(CHORDS)*BAR*SR)
rng=np.random.default_rng(42)
stems={k:np.zeros(N,dtype=np.float32) for k in ('bass','guitar','drums')}
def add(track,start,sound,volume=1):
    p=round(start*SR)
    if p>=N:return
    length=min(len(sound),N-p)
    if length>0:stems[track][p:p+length]+=sound[:length]*volume
def hz(m):return 440*2**((m-69)/12)
def pluck(m,duration,kind):
    t=np.arange(max(1,round(duration*SR)))/SR
    f=hz(m)
    if kind=='bass':
        signal=np.sin(2*np.pi*f*t)+.23*np.sin(4*np.pi*f*t)*np.exp(-t*8)+.08*np.sin(6*np.pi*f*t)*np.exp(-t*14)
        env=(1-np.exp(-t*130))*np.exp(-t*2.8)
    else:
        signal=sum(np.sin(2*np.pi*f*j*t)*np.exp(-t*(4+j*3))/(j**1.3) for j in range(1,7))
        env=(1-np.exp(-t*200))*np.exp(-t*7)
    return (signal*env).astype(np.float32)
def brush(duration,accent):
    count=round(duration*SR)
    raw=rng.normal(0,1,count)
    # low-energy colored noise with a smooth brush stroke envelope
    smooth=np.convolve(raw,np.ones(7)/7,'same')
    t=np.arange(count)/SR
    env=np.sin(np.pi*np.minimum(t/duration,1))**2
    return (smooth*env*accent).astype(np.float32)
catalog={'version':1,'description':'Original procedurally rendered demonstration stems, not AI-generated acoustic performances','tracks':[]}
os.makedirs('audio/stems',exist_ok=True)
for slug,title,progression,style,bpm,chords,roots in ARRANGEMENTS:
    BPM=bpm
    CHORDS=chords
    ROOTS=roots
    BAR=240/BPM
    N=round(len(CHORDS)*BAR*SR)
    stems={k:np.zeros(N,dtype=np.float32) for k in ('bass','guitar','drums')}
    for bar,root in enumerate(ROOTS):
        base=bar*BAR
        beat=60/BPM
        for b in range(4):
            nextroot=ROOTS[(bar+1)%len(ROOTS)]
            choices=[root,root+7,root+9,nextroot-1 if nextroot>=root else nextroot+1]
            note=choices[b]-12
            add('bass',base+b*beat+(0.012 if b%2 else 0),pluck(note,min(.58,beat*.85),'bass'),.27 if b else .31)
        minor=CHORDS[bar].startswith(('Am','Dm','Em','Bm'))
        intervals=[0,3 if minor else 4,6 if 'b5' in CHORDS[bar] else 7,10]
        for b in ((0,2) if style=='bossa' else (1,3)):
            for j,interval in enumerate(intervals[1:]):
                add('guitar',base+b*beat+j*.014+.018,pluck(root+12+interval,.26,'guitar'),.039 if b==1 else .047)
        for eighth in range(8):
            swing=(.12*beat if eighth%2 else 0) if style!='bossa' else 0
            add('drums',base+eighth*beat/2+swing,brush(.11,.28 if eighth%2 else .44),.23)
        for b in (1,3):
            add('drums',base+b*beat,brush(.18,.85),.26)
    for name,a in stems.items():
        peak=max(1,float(np.max(np.abs(a)))/.85)
        pcm=(np.clip(a/peak,-1,1)*32767).astype('<i2')
        with wave.open('audio/stems/'+slug+'-'+name+'.wav','wb') as w:
            w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes(pcm.tobytes())
    catalog['tracks'].append({'id':slug+'-demo','title':title+' — rendered demo','progression':progression,'style':style,'bpm':BPM,'bars':CHORDS,'barSeconds':BAR,'durationSeconds':len(CHORDS)*BAR,'source':'Original procedural synthesis; no external samples','stems':{name:'audio/stems/'+slug+'-'+name+'.wav' for name in stems}})
with open('audio/catalog.json','w') as f:json.dump(catalog,f,indent=2)
print('Generated',len(catalog['tracks']),'arrangements')
