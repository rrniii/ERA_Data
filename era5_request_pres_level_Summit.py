def main():
    import cdsapi
    import numpy as np
    import os
    c = cdsapi.Client()

    outdir = '/Volumes/Neely/GREENLAND/ICECAPSarchive/ERA_5/73N_39_5W_72N_35_5W/'

    os.chdir(outdir)
    start_year = 1979
    stop_year = 2020
    years = np.arange(start_year, stop_year + 1)
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    for year in years:
        for month in months:
            for day in days:
                file_name = outdir+'era5_pres_level_Summit_' + str(year) + str(month) + str(day) + '.nc'
                print(file_name)

                if os.path.isfile(file_name)==True:
                    print('exists')
                    continue
                else:
                    try:
                        c.retrieve('reanalysis-era5-pressure-levels',
                                   {
                                       'product_type': 'reanalysis',
                                       'format': 'netcdf',
                                       'variable': ['divergence', 'fraction_of_cloud_cover', 'geopotential',
                                                    'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity',
                                                    'specific_cloud_ice_water_content',
                                                    'specific_cloud_liquid_water_content', 'specific_humidity',
                                                    'specific_rain_water_content',
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
                                                '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', ],
                                       'area': [73, -39.5, 72, -37.5, ],
                                   }, file_name)
                    except Exception:
                        continue


if __name__ == '__main__':
    main()
