def main():
    import cdsapi
    import numpy as np
    import os
    c = cdsapi.Client()

    outdir = '/Volumes/Neely/GREENLAND/ICECAPSarchive/ERA_5/73N_39_5W_72N_35_5W/raw_data/surface/'

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
                file_name = outdir + 'era5_surface_Summit_' + str(year) + str(month) + str(day) + '.nc'
                print(file_name)

                if os.path.isfile(file_name)==True:
                    print('exists')
                    continue
                else:

                    try:
                        c.retrieve('reanalysis-era5-single-levels',
                                   {'product_type': 'reanalysis',
                                    'format': 'netcdf',
                                    'variable': ['100m_u_component_of_wind', '100m_v_component_of_wind',
                                                 '10m_u_component_of_wind', '10m_v_component_of_wind',
                                                 '10m_wind_gust_since_previous_post_processing',
                                                 'instantaneous_10m_wind_gust',
                                                 '2m_dewpoint_temperature', '2m_temperature',
                                                 'maximum_2m_temperature_since_previous_post_processing',
                                                 'minimum_2m_temperature_since_previous_post_processing',
                                                 'skin_temperature',
                                                 'boundary_layer_dissipation', 'boundary_layer_height',
                                                 'mean_boundary_layer_dissipation', 'trapping_layer_top_height',
                                                 'clear_sky_direct_solar_radiation_at_surface',
                                                 'cloud_base_height', 'total_cloud_cover',
                                                 'high_cloud_cover', 'medium_cloud_cover', 'low_cloud_cover',
                                                 'convective_snowfall', 'convective_snowfall_rate_water_equivalent',
                                                 'large_scale_snowfall', 'large_scale_snowfall_rate_water_equivalent',
                                                 'friction_velocity',
                                                 'temperature_of_snow_layer',
                                                 'ice_temperature_layer_1', 'ice_temperature_layer_2',
                                                 'ice_temperature_layer_3', 'ice_temperature_layer_4',
                                                 'mean_sea_level_pressure', 'surface_pressure',
                                                 'near_ir_albedo_for_diffuse_radiation',
                                                 'near_ir_albedo_for_direct_radiation',
                                                 'snow_albedo',
                                                 'orography',
                                                 'precipitation_type',
                                                 'snow_density', 'snow_depth',
                                                 'snow_evaporation', 'snowfall', 'snowmelt',
                                                 'surface_latent_heat_flux', 'surface_sensible_heat_flux',
                                                 'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky',
                                                 'surface_net_thermal_radiation',
                                                 'surface_net_thermal_radiation_clear_sky',
                                                 'surface_solar_radiation_downward_clear_sky',
                                                 'surface_solar_radiation_downwards',
                                                 'surface_thermal_radiation_downward_clear_sky',
                                                 'surface_thermal_radiation_downwards',
                                                 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water',
                                                 'total_column_rain_water', 'total_column_snow_water',
                                                 'total_column_supercooled_liquid_water', 'total_column_water',
                                                 'total_column_water_vapour', 'total_precipitation',
                                                 'total_column_ozone',
                                                 ],
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
