# Stored Procedure: `prc_asd_Update_DoanhSoThucChay_HopDongChiTiet_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-04-03 18:05:57.743000
- **Ngày sửa cuối**: 2020-04-04 10:14:01.863000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql



CREATE PROCEDURE [dbo].[prc_asd_Update_DoanhSoThucChay_HopDongChiTiet_v2]
AS
    BEGIN
	   -- SET NOCOUNT ON added to prevent extra result sets from
	   -- interfering with SELECT statements.
        SET NOCOUNT ON;
        DECLARE @NgayThucChayMax_HD DATETIME ,
            @NgayThucChayMax_TCDT DATETIME;
        DECLARE @Table_contract_detail TABLE
            (
              CONTRACT_ID INT ,
              CONTRACT_DETAIL_ID INT
            );
        DECLARE @Table_tc TABLE
            (
              CONTRACT_ID INT ,
              CONTRACT_DETAIL_ID INT ,
              MONEY_REAL_RUNING FLOAT ,
              DATE_REAL_RUNING DATE
            );
		DECLARE @Table_tc_doitru TABLE
            (
              CONTRACT_DETAIL_ID INT 
            );
	   --NOTE: TUNG PHAI KHOI TAO LAI DU LIEU TU DAU VA TU CAP NHAT LẠI NGAY TREN TABLE CONFIG

	   --B1: LAY THONG TIN NGAY THUC CHAY MAX TREN TABLE CONFIG
        SET @NgayThucChayMax_HD = '2020-03-31'
		--( SELECT  MAX(ACTUAL_RUN_DATE)
  --                                  FROM    [ASD14].contract.dbo.CONTRACT_INFO_DATE_RUNNING_REAL
  --                                );
	   --B2: XAC DINH DANH SACH CONTRACT_DETAILS_ID CO PHAT SINH THUC CHAY TU NGAY THUC CHAY MAX TREN TABLE CONFIG TREN ABM_DATA_RELEASE
        INSERT  INTO @Table_contract_detail
                SELECT  HopDongID ,
                        HopDongChiTietREF
                FROM    [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinh
                WHERE   1 = 1
                        AND DmSanPhamREF NOT IN ( 299, 337, 144, 585, 628 )
                        AND TrangThaiHopDong <> 3
                        AND NgayThucHien > @NgayThucChayMax_HD
                GROUP BY HopDongID ,
                        HopDongChiTietREF
                UNION ALL
                SELECT  HopDongID ,
                        HopDongChiTietREF
                FROM    [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket tcdt
                WHERE   1 = 1
                        AND tcdt.TrangThaiHopDong <> 3
                        AND tcdt.DmSanPhamREF IN ( 299, 337, 144, 585, 628 )
                        AND NgayThucHien > @NgayThucChayMax_HD
                GROUP BY HopDongID ,
                        HopDongChiTietREF;
	   -- NEU TON TAI BAN GHI PHAT SINH THI MOI THUC HIEN CAC BUOC TIEP THEO
        IF EXISTS ( SELECT  1
                    FROM    @Table_contract_detail )
            BEGIN
			 --B3: LAY THONG TIN THUC CHAY CUA CAC CONTRACT_DETAILS_ID TREN ABM_DATA_RELEASE (CHU Y LA KHONG CAN THEO THOI GIAN)
                INSERT  INTO @Table_tc
                        ( CONTRACT_ID ,
                          CONTRACT_DETAIL_ID ,
                          MONEY_REAL_RUNING ,
                          DATE_REAL_RUNING
			         )
				    SELECT * FROM
				    (
                        SELECT  HopDongID ,
                                HopDongChiTietREF ,
                                SUM(ISNULL(ThanhTienSauTrietKhauThucChay, 0)
                                    + ISNULL(GiaTriThayDoi, 0)) ThanhTienThucChay ,
                                MAX(NgayThucHien) NgayThucHien
                        FROM    [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinh
                        WHERE   1 = 1
                                AND DmSanPhamREF NOT IN ( 299, 337, 144, 585,
                                                          628 )
                                AND TrangThaiHopDong <> 3
                                AND HopDongChiTietREF IN (
                                SELECT  CONTRACT_DETAIL_ID
                                FROM    @Table_contract_detail GROUP BY CONTRACT_DETAIL_ID )
						  
                        GROUP BY HopDongID ,
                                HopDongChiTietREF
				    )A
				    
					-- where a.ThanhTienThucChay <> 0

                        UNION ALL
				    SELECT * FROM
				    (
                        SELECT  HopDongID ,
                                HopDongChiTietREF ,
                                SUM(ISNULL(ThanhTienSauTrietKhauThucChay, 0)
                                    + ISNULL(GiaTriThayDoi, 0)) ThanhTienThucChay ,
                                MAX(NgayThucHien) NgayThucHien
                        FROM    [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket tcdt
                        WHERE   1 = 1
                                AND tcdt.TrangThaiHopDong <> 3
                                AND tcdt.DmSanPhamREF IN ( 299, 337, 144, 585,
                                                           628 )
                                AND HopDongChiTietREF IN (
                                SELECT  CONTRACT_DETAIL_ID
                                FROM    @Table_contract_detail GROUP BY CONTRACT_DETAIL_ID)
                        GROUP BY HopDongID ,
                                HopDongChiTietREF
				    )B 
					--WHERE B.ThanhTienThucChay <> 0;
			 --B4: CAP NHAT GIA TRI THUC CHAY CUA CAC CONTRACT_DETAILS_ID DA LAY VAO TABLE CONTRACT_DETAILS
      --          UPDATE  dbo.CONTRACT_DETAILS
      --          SET     MONEY_REAL_RUNING = ISNULL(tc.MONEY_REAL_RUNING, 0) ,
      --                  DATE_REAL_RUNING = tc.DATE_REAL_RUNING
      --          FROM    dbo.CONTRACT_DETAILS ctdt
      --                  INNER JOIN 
						--(
						insert into Table_tc
							SELECT tc.CONTRACT_ID, tc.CONTRACT_DETAIL_ID
							, SUM(tc.MONEY_REAL_RUNING) AS MONEY_REAL_RUNING
							, MAX(tc.DATE_REAL_RUNING) AS DATE_REAL_RUNING 
							, Null IS_REAL_RUNING
							,hdct.MONEY_TURNOVER
							FROM @Table_tc tc left join [asd14].contract.dbo.contract_details hdct on tc.CONTRACT_DETAIL_ID = hdct.ID
							GROUP BY tc.CONTRACT_ID, tc.CONTRACT_DETAIL_ID,hdct.MONEY_TURNOVER
						--) 
						--tc ON ctdt.ID = tc.CONTRACT_DETAIL_ID
      --                      AND ctdt.CONTRACT_ID = tc.CONTRACT_ID
      --          WHERE   ctdt.DELETED_STATUS = 0;
				--COMMENT LAI PHAN LOAI DIEU KIEN MUA NGOAI THEO YEU CAU CUA TUYET 2018-11-12
                        --AND NOT ( ctdt.PRODUCT_FORMALITY_ID = 13
                        --          OR EXISTS ( SELECT    1
                        --                      FROM      dbo.CONTRACT_DETAIL_PRODUCT_PROPERTIES ctdtp
                        --                      WHERE     1 = 1
                        --                                AND ctdtp.DELETED_STATUS = 0
                        --                                AND ( ctdtp.VALUE = 18
                        --                                      AND ctdtp.PRODUCT_CONFIG_PROPERTY_ID = 5
                        --                                    )
                        --                                AND ctdtp.CONTRACT_DETAIL_ID = ctdt.ID )
                        --        ); 

			 --B5: CAP NHAT LAI THONG TIN NGAY THUC CHAY MAX TREN TABLE CONFIG
                --SET @NgayThucChayMax_HD = ( SELECT  MAX(DATE_REAL_RUNING)
                --                            FROM    @Table_tc
                --                          );
			 --UPDATE CHO TABLE CONFIG
                --IF ( @NgayThucChayMax_HD IS NOT NULL )
                --    BEGIN
                --        UPDATE  CONTRACT_INFO_DATE_RUNNING_REAL
                --        SET     ACTUAL_RUN_DATE = @NgayThucChayMax_HD; 
                --    END;

			 --B6: CAP NHAT TRANG THAI THUC CHAY
                UPDATE  dbo.Table_tc
                SET     IS_REAL_RUNING = CASE WHEN ABS(ISNULL(ctdt.MONEY_REAL_RUNING,
                                                              0)
                                                       - ISNULL(ctdt.MONEY_TURNOVER,
                                                              0)) <= 100 
															  and (MONEY_TURNOVER > 0)
                                              THEN 3
                                              WHEN ABS(ISNULL(ctdt.MONEY_REAL_RUNING,
                                                              0)
                                                       - ISNULL(ctdt.MONEY_TURNOVER,
                                                              0)) > 100
                                                   AND ( ( ISNULL(ctdt.MONEY_REAL_RUNING,
                                                              0)
                                                           - ISNULL(ctdt.MONEY_TURNOVER,
                                                              0) ) <= 100 )
												   AND ctdt.MONEY_REAL_RUNING <> 0 --bo sung ngay 06/04/2018
                                              THEN 2
                                              WHEN ISNULL(ctdt.MONEY_REAL_RUNING,
                                                          0) > ISNULL(ctdt.MONEY_TURNOVER,
                                                              0) THEN 3
                                              ELSE 0
                                         END
                FROM    dbo.Table_tc ctdt
                        INNER JOIN @Table_tc tc ON ctdt.CONTRACT_DETAIL_ID = tc.CONTRACT_DETAIL_ID
                                                   AND ctdt.CONTRACT_ID = tc.CONTRACT_ID;
            END;
			
			--- Những phân bổ về bằng 0
			INSERT INTO @Table_tc_doitru SELECT DISTINCT CONTRACT_DETAIL_ID  FROM @Table_tc WHERE ROUND(MONEY_REAL_RUNING,0) = 0
			--- những phân bổ về = 0 vẫn có trong thực cheo
			insert into Table_tc (CONTRACT_DETAIL_ID,[IS_REAL_RUNING],DATE_REAL_RUNING)
			select b.HopDongChiTietREF,1, getdate() from 
			(
				SELECT Contract_Detail_Id HopDongChiTietREF FROM [asd14].[ThucTreo].[dbo].[ThucTreo_ChiPhi]  /* Tuyetnta sửa nguồn thực treo*/
				WHERE deletedstatus = 0 AND Contract_Detail_Id IN (SELECT CONTRACT_DETAIL_ID FROM @Table_tc_doitru)
				UNION 
				SELECT Contract_Detail_Id HopDongChiTietREF FROM [asd14].[ThucTreo].[dbo].[ThucTreo_PR]  /* Tuyetnta sửa nguồn thực treo*/
				WHERE Deleted_Status = 0 AND Contract_Detail_Id IN (SELECT CONTRACT_DETAIL_ID FROM @Table_tc_doitru)
					UNION 
				SELECT Contract_Detail_Id HopDongChiTietREF FROM [asd14].[ThucTreo].[dbo].[ThucTreo]  /* Tuyetnta sửa nguồn thực treo*/
				WHERE Deleted_Status = 0 AND Contract_Detail_Id IN (SELECT CONTRACT_DETAIL_ID FROM @Table_tc_doitru)
			) b 
		
    END;







```
