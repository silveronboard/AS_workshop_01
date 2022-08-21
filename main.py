import matplotlib
import matplotlib.pyplot as plt
import pandas
import numpy as np
## reading file
folder = 'z:\Seismic\Geophysical\99_Personal\Andrey\pyws'
folder_sm = 'z:\Seismic\Geophysical\99_Personal\Andrey\pyws\sm'
section_rms=[]
for seq in range (1,34):
    file = 'section_' + str(seq) + '.txt'
    fpath = folder + '\\' + file
    with open (fpath,'r') as file_1:
        lines=file_1.readlines()
        for line in lines:
            sequence_number = line.split()[0]
            good_sps_number = line.split()[1]
            streamer_number = line.split()[3]
            section_number = line.split()[4]
            section_per_cable = line.split()[5]
            section_serial = line.split()[6]
            raw_sesitivity = line.split()[-1]
#            print("sequence_number: " + sequence_number, "good_sps_number: " + good_sps_number,"streamer_number: " + streamer_number,"section_number: " + section_number,\
#                  "section_per_cable: " + section_per_cable, 'section_serial: '+ section_serial, 'raw_sensitivity: '+ raw_sesitivity)
            if int(section_number) in range(1,54):
                pair = []
                pair.append(int(sequence_number))
                pair.append(float(section_per_cable))
                pair.append(float(raw_sesitivity))
                section_rms.append(pair)
        file_1.closed
#print (section_rms)
data = np.array(section_rms)
x,y,z = data.T
axes=plt.gca()
axes.set_aspect( (54/int(sequence_number)*0.9) )
plt.scatter(x, y, c=z,cmap='jet',vmin=7000,vmax=13000,marker='s',)
plt.title('Raw Sensitivity')
plt.xlabel('sequence')
plt.ylabel('section')
plt.show()
print (x,y,z)

################################ smoothed #############################################
section_rms=[]
for seq in range (1,34):
    seq = str(seq).zfill(3)
    file = 'scalar_seq_' + str(seq) + '.txt'
    fpath = folder_sm + '\\' + file
    with open (fpath,'r') as file_1:
        lines=file_1.readlines()
        for line in lines:
            if line [0] != "H":
                sequence_number = str(int(seq))
                #good_sps_number = line.split()[1]
                #streamer_number = line.split()[1]
                section_number = line.split()[1]
                #section_per_cable = line.split()[5]
                #section_serial = line.split()[6]
                sm_sesitivity = line.split()[-1]
    #            print("sequence_number: " + sequence_number, "good_sps_number: " + good_sps_number,"streamer_number: " + streamer_number,"section_number: " + section_number,\
    #                  "section_per_cable: " + section_per_cable, 'section_serial: '+ section_serial, 'raw_sensitivity: '+ raw_sesitivity)
                if int(section_number) in range(1,54):
                    pair = []
                    pair.append(int(sequence_number))
                    pair.append(float(section_number))
                    pair.append(float(sm_sesitivity))
                    section_rms.append(pair)
                    print (sequence_number, section_number, sm_sesitivity)
        file_1.closed
#print (section_rms)
data = np.array(section_rms)
x,y,z = data.T
axes=plt.gca()
axes.set_aspect( (54/int(sequence_number)*0.9) )
plt.scatter(x, y, c=z,cmap='jet',vmin=7000,vmax=13000,marker='s',)
plt.title('Smoothed Sensitivity')
plt.xlabel('sequence')
plt.ylabel('section')
plt.show()
plt.xlabel('sequence')
plt.ylabel('section')
print (x,y,z)