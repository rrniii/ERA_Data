def main():
    import cdsapi
    import numpy as np

    c = cdsapi.Client()

    start_year = 1979
    stop_year = 2020

    years = np.arange(start_year, stop_year + 1)

    for y in years:
        filename='ERA5_Chapel_Allerton'+str(y)+'.nc'
        c.retrieve(
            'reanalysis-era5-single-levels',
            {'product_type': 'reanalysis',
             'format': 'netcdf',
             'variable': ['100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_wind',
                          '10m_v_component_of_wind', '2m_dewpoint_temperature', '2m_temperature',
                          'convective_precipitation', 'instantaneous_10m_wind_gust', 'large_scale_precipitation',
                          'snowfall', 'surface_pressure', 'total_cloud_cover', 'total_precipitation',],
             'year': str(y),
             'month': [ '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',],
             'day': [
                    '01', '02', '03',
                    '04', '05', '06',
                    '07', '08', '09',
                    '10', '11', '12',
                    '13', '14', '15',
                    '16', '17', '18',
                    '19', '20', '21',
                    '22', '23', '24',
                    '25', '26', '27',
                    '28', '29', '30',
                    '31',],
             'time': [
                    '00:00', '01:00', '02:00',
                    '03:00', '04:00', '05:00',
                    '06:00', '07:00', '08:00',
                    '09:00', '10:00', '11:00',
                    '12:00', '13:00', '14:00',
                    '15:00', '16:00', '17:00',
                    '18:00', '19:00', '20:00',
                    '21:00', '22:00', '23:00',],
             'area': [53.85, -1.56, 53.8,-1.52,],
            }, filename)

if __name__ == '__main__':
    main()
