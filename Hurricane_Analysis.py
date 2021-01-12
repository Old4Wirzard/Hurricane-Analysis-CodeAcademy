
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_function(damages):
    update_damages = []
    for i in damages:
        if i == 'Damages not recorded':
            #update_damages.append(i)
            update_damages.append(0)
        elif 'M' in i:
            value = i.strip('M')
            value = float(value)
            update_damages.append(value*1000000)
        else:
            value = i.strip('B')
            value = float(value)
            update_damages.append(value*1000000000)
    return update_damages
#print(update_function(damages))

# write your construct hurricane dictionary function here:
def cr_dic():
    H_data ={}
    j = 0
    for i in names:
        H_data[i] = {'Name': i, 'Months': months[j], 'Year': years[j],'Max Sustained Winds' :max_sustained_winds[j], 'Areas Affected':areas_affected[j], 'Damage': damages[j], 'Deaths' : deaths[j]}
        j += 1
    return H_data#
#print(cr_dic())

# write your construct hurricane by year dictionary function here:
def cr_dt():
    H_data_year ={}
    j = 0
    for i in years:
        H_data_year[i] = {}
        #H_data_year[i] = {'Name': names[j], 'Months': month 
        H_data_year[i]['Month'] = months[j]
        H_data_year[i]['Year'] = years[j]
        H_data_year[i]['Max Sustained Winds'] = max_sustained_winds[j]
        H_data_year[i]['Areas Affected'] = areas_affected[j]
        H_data_year[i]['Damage'] = damages[j]
        H_data_year[i]['Deaths'] = deaths[j]
        j += 1
    return H_data_year
#print(cr_dt())                
# write your count affected areas function here:
def c_aff():
    H_data_aff = {}
    areas_all =[]
    for i in range(len(areas_affected)):
        areas_all += areas_affected[i]
    for i in areas_all:
        H_data_aff[i] = areas_all.count(i)
    return H_data_aff
#print(c_aff())
# write your find most affected area function here:
def m_aff():
    new_ls = c_aff()
    new_ls_2 = [ ]
    for i in new_ls:
        new_ls_2.append([new_ls.get(i), i])
    new_ls_2.sort()
    print('The most affected area is {} by {} times.'.format( new_ls_2[-1][1],  new_ls_2[-1][0]))
#m_aff()
# write your greatest number of deaths function here:
def d_aff():
    new_ls = list(zip(deaths,names))
    new_ls.sort()
    print('The Huracan that cause the major number of deaths was {} by {} deaths.'.format( new_ls[-1][1],  new_ls[-1][0]))
#d_aff()
# write your catgeorize by mortality function here:
def mor():
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for i in range(len(deaths)):
        if deaths[i] == 0 :
           hurricanes_by_mortality[0].append(names[i])
        elif deaths[i] <= 100:
           hurricanes_by_mortality[1].append(names[i])
        elif deaths[i] <= 500:
            hurricanes_by_mortality[2].append(names[i])
        elif deaths[i] <= 1000:
            hurricanes_by_mortality[3].append(names[i])
        elif deaths[i] <= 10000:
            hurricanes_by_mortality[4].append(names[i])
        elif deaths[i] > 10000:
            hurricanes_by_mortality[5].append(names[i])
    print(hurricanes_by_mortality)
#mor()            
# write your greatest damage function here:
def dam_aff():
    update_dam = update_function(damages)
    new_ls = list(zip(update_dam,names))
    new_ls.sort()
    print('The greaest damge was cause by {} by {} dollars.'.format( new_ls[-1][1],  new_ls[-1][0]))
#dam_aff()
# write your catgeorize by damage function here:
def dam():
    update_dam = update_function(damages)
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
    for i in range(len(deaths)):
        #print(update_dam[i])
        if update_dam[i] == 0 :
           hurricanes_by_damage[0].append(names[i])
        elif update_dam[i] <= 100000000:
           hurricanes_by_damage[1].append(names[i])
        elif update_dam[i] <= 10000000000:
            hurricanes_by_damage[2].append(names[i])
        elif update_dam[i] <= 10000000000:
            hurricanes_by_damage[3].append(names[i])
        elif update_dam[i] <= 50000000000:
            hurricanes_by_damage[4].append(names[i])
        elif update_dam[i] > 50000000000:
            hurricanes_by_damage[5].append(names[i])
    print(hurricanes_by_damage)
dam()