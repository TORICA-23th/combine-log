import csv
import os
import sys

directory = input("directory=")
start = int(input("start="))
end = int(input("end="))

buffer = []
header = ["time_ms","data_main_bno_accx_mss","data_main_bno_accy_mss","data_main_bno_accz_mss",
"data_main_bno_qw","data_main_bno_qx","data_main_bno_qy","data_main_bno_qz","data_main_bno_roll","data_main_bno_pitch","data_main_bno_yaw","data_main_dps_pressure_hPa","data_main_dps_temperature_deg","data_main_dps_altitude_m","data_under_dps_pressure_hPa","data_under_dps_temperature_deg","data_under_dps_altitude_m","data_under_urm_altitude_m","data_air_dps_pressure_hPa","data_air_dps_temperature_deg","data_air_dps_altitude_m","data_air_sdp_differentialPressure_Pa","data_air_sdp_airspeed_mss","data_ics_angle","data_main_gps_hour","data_main_gps_minute","data_main_gps_second.centisecond","data_main_gps_latitude_deg","data_main_gps_longitude_deg","data_main_gps_altitude_m"]

flag = False
err = False


for filenum in range(start, end+1):
    filepass = directory + os.sep + "LOG" + str(filenum).zfill(4) + ".csv"

    try:
        with open(filepass) as fr:
            reader = csv.reader(fr, delimiter=',')
            l = [row for row in reader]
            if(flag):
                if(buffer[-1][-1] == ''):
                    del buffer[-1][-1]
                    buffer[-1] += l[0]
                    buffer += l[1:]
                else:
                    buffer += l
            else:
                buffer += l
                flag = True
    except:
        print("Couldn't open file.")
        input("enterで終了")
        sys.exit()

try:
    os.mkdir(directory + os.sep + "out")
except FileExistsError:
    pass

directory += os.sep + "out"
result_filepass = directory + os.sep +"result_" + str(start) + "_to_" + str(end) + ".csv"
try:
    with open(result_filepass,'w', newline='') as fw:
        writer_header = csv.writer(fw)
        writer_main = csv.writer(fw)
        writer_header.writerow(header)
        writer_main.writerows(buffer)
except:
    print("Coudln't make file.")
    input("enterで終了")
    sys.exit()

print("正常に結合後のファイルが作成されました")
print(result_filepass)
input("enterで終了")


