def main():
    import cdsapi
    import numpy as np
    import os
    import pandas as pd
    import math

    def quarter_up(x):
        return math.ceil(x * 4) / 4

    def quarter_down(x):
        return math.floor(x * 4) / 4

    c = cdsapi.Client()

    file = '/Volumes/Neely/BioDAR/ERA5/sites of light and suction traps.xlsx'
    light_traps = pd.read_excel(file, header=0, sheet_name='Light traps')
    number_of_traps = len(light_traps['Lat'])
    areas = []
    trap_name = []

    for a in range(0, number_of_traps):
        lats = [quarter_up(light_traps['Lat'][a]), quarter_down(light_traps['Lat'][a])]
        longs = [quarter_up(light_traps['Long'][a]), quarter_down(light_traps['Long'][a])]
        areas.append([max(lats), min(longs), min(lats), max(longs), ])
        trap_name.append(light_traps['Trap name'][a].replace(" ", "_"))

    start_year = 1979
    stop_year = 2020

    years = np.arange(start_year, stop_year+1)
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    for year in years:
        for month in months:
            for day in days:
                for idx, area in enumerate(areas):
                    try:
                        outdir = '/Volumes/Neely/BioDAR/ERA5/Myrna_TrapLocations_0_25_Box/light_traps/pres_levels/' \
                                 + str(trap_name[idx]) + '/'
                        if not os.path.exists(outdir):
                            os.makedirs(outdir)
                        file_name = outdir + 'era5_pres_level_' + str(trap_name[idx]) + '_' + \
                                    str(year) + str(month) + str(day) + '.nc'
                        print(str(trap_name[idx]), area)

                        print(file_name)

                        if os.path.isfile(file_name) == True:
                            print('exists')
                            continue

                        else:
                            c.retrieve('reanalysis-era5-pressure-levels',
                                       {
                                           'product_type': 'reanalysis',
                                           'format': 'netcdf',
                                           'variable': ['divergence', 'fraction_of_cloud_cover', 'geopotential',
                                                        'ozone_mass_mixing_ratio', 'potential_vorticity',
                                                        'relative_humidity', 'specific_cloud_ice_water_content',
                                                        'specific_cloud_liquid_water_content',
                                                        'specific_humidity', 'specific_rain_water_content',
                                                        'specific_snow_water_content', 'temperature', 'u_component_of_wind',
                                                        'v_component_of_wind', 'vertical_velocity', 'vorticity',
                                                        ],
                                           'pressure_level': ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100',
                                                              '125', '150', '175', '200', '225', '250', '300', '350', '400',
                                                              '450', '500', '550', '600', '650', '700', '750', '775', '800',
                                                              '825', '850', '875', '900', '925', '950', '975', '1000', ],
                                           'year': [str(year)],
                                           'month': [month],
                                            'day': [day],
                                           'time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00',
                                                    '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00',
                                                    '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',
                                                    ],
                                           'area': area,
                                       }, file_name)
                    except:
                        continue


if __name__ == '__main__':
    main()
