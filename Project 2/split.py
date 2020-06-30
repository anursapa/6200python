        def insertSoups:
            SoupId = int(record[13])
            Type = int(record[14])
            Vendor = int(record[15])
            Mode = int(record[16])
            Style = int(record[17])
        def insertDays:
            DoY = int(record[1])
            DoW = int(record[2])
            Holiday = int(record[3])
            Weather = int(record[4])
        def insertStores:
            StoreId = int(record[5])
            Location = int(record[6])
            Elevation = int(record[7])
            Size  = int(record[8])
        def insertPromotions:
            PtomoId = int(record[18])
            Medium = int(record[19])
            Target = int(record[20])
            Interval = int(record[21])    
        def insertManagers:
            MgrId = int(record[9])
            MgrName = int(record[10])
            Grade = int(record[11])
            Years = int(record[12])

        def insertSales:
            TrxId = int(record[0])
            DoY = int(record[1])
            SoupId = int(record[13])
            
            
            
            
            Sales = float(record[22])
            row = [TrxId, DoY, DoW, Holiday, Weather, StoreId, Location, 
            Elevation, Size, MgrId, MgrName, Grade, Years, SoupId, Type,
            Vendor, Mode, Style, PtomoId, Medium, Target, Interval, Sales]
            