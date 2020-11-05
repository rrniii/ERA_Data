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
    stop_year = 2021

    years = np.arange(start_year, stop_year + 1)
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    for year in years:
        for month in months:
            for day in days:
                for idx, area in enumerate(areas):
                    try:
                        outdir = '/Volumes/Neely/BioDAR/ERA5/Myrna_TrapLocations_0_25_Box/light_traps/surface/' \
                                 + str(trap_name[idx]) + '/'
                        if not os.path.exists(outdir):
                            os.makedirs(outdir)
                        file_name = outdir + 'era5_surface_' + str(trap_name[idx]) + '_' + \
                                    str(year) + str(month) + str(day) + '.nc'
                        print(str(trap_name[idx]), area)

                        print(file_name)

                        if os.path.isfile(file_name) == True:
                            print('exists')
                            continue

                        else:
                            c.retrieve('reanalysis-era5-single-levels',
                                       {
                                           'product_type': 'reanalysis',
                                           'format': 'netcdf',
                                           'variable': ['10m_u_component_of_wind', '10m_v_component_of_wind',
                                                        '10m_wind_gust_since_previous_post_processing',
                                                        '2m_dewpoint_temperature', '2m_temperature',
                                                        'skin_temperature',
                                                        'boundary_layer_dissipation',
                                                        'boundary_layer_height',
                                                        'cloud_base_height',
                                                        'evaporation', 'potential_evaporation',
                                                        'leaf_area_index_high_vegetation',
                                                        'leaf_area_index_low_vegetation',
                                                        'low_vegetation_cover', 'high_vegetation_cover',
                                                        'type_of_high_vegetation', 'type_of_low_vegetation',
                                                        'maximum_2m_temperature_since_previous_post_processing',
                                                        'minimum_2m_temperature_since_previous_post_processing',
                                                        'mean_sea_level_pressure',
                                                        'orography',
                                                        'runoff', 'sub_surface_runoff', 'surface_runoff',
                                                        'surface_latent_heat_flux',
                                                        'surface_net_solar_radiation',
                                                        'surface_net_thermal_radiation', 'surface_pressure',
                                                        'surface_sensible_heat_flux',
                                                        'surface_solar_radiation_downwards',
                                                        'surface_thermal_radiation_downwards',
                                                        'total_cloud_cover',
                                                        'total_column_rain_water',
                                                        'precipitation_type', 'total_precipitation',
                                                        ],
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
