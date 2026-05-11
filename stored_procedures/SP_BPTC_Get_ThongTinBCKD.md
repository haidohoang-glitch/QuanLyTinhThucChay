# Stored Procedure: `BPTC_Get_ThongTinBCKD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.820000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@LoaiBaoCaoKinhDoanh` | `int(4)` | No |
| `@NguoiLap` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql



CREATE PROCEDURE [dbo].[BPTC_Get_ThongTinBCKD]
    @NgayBatDau DATETIME ,
    @NgayKetThuc DATETIME ,
    @LoaiBaoCaoKinhDoanh INT , --1 : BÁO CÁO TUẦN, 2: BÁO CÁO THÁNG
    @NguoiLap NVARCHAR(255)
AS 
    BEGIN
	
        DECLARE @TenLoaiBaoCaoKinhDoanh NVARCHAR(200)		
        DECLARE @TenBaoCaoKinhDoanh NVARCHAR(200)	
        DECLARE @BPTC_ThongTinBCKDID INT
        DECLARE @BPTC_TenBaoCao NVARCHAR(100)
	
        SET @TenLoaiBaoCaoKinhDoanh = CASE @LoaiBaoCaoKinhDoanh
                                        WHEN 1 THEN N'Báo cáo tuần'
                                        ELSE N'Báo cáo tháng'
                                      END
	          
        SET @TenBaoCaoKinhDoanh = @TenLoaiBaoCaoKinhDoanh + '_'
            + CONVERT(NVARCHAR(50), @NgayBatDau, 103) + '_'
            + CONVERT(NVARCHAR(50), @NgayKetThuc, 103) + '_' + @NguoiLap + '_'
            + CONVERT(NVARCHAR(50), GETDATE(), 113)	
	
	-- INSERT BPTC_ThongTinBCKD
PRINT CONVERT(TIME,GETDATE())
        INSERT  INTO dbo.BPTC_ThongTinBCKD
                ( LoaiBaoCaoKinhDoanh ,
                  TenLoaiBaoCaoKinhDoanh ,
                  TenBaoCaoKinhDoanh ,
                  ThoiGianBatDau ,
                  ThoiGianKetThuc ,
                  NguoiLap ,
                  NgayLap ,
                  TrangThaiPheDuyet ,
                  NguoiPheDuyet ,
                  NgayPheDuyet ,
                  CreatedBy ,
                  CreatedAt ,
                  LastModifiedBy ,
                  LastModifiedAt ,
                  DeleteStatus ,
                  PrintStatus ,
                  RecordStatus
	          )
        VALUES  ( @LoaiBaoCaoKinhDoanh , -- LoaiBaoCaoKinhDoanh - nvarchar(100)
                  @TenLoaiBaoCaoKinhDoanh , -- TenLoaiBaoCaoKinhDoanh - nvarchar(100)
                  @TenBaoCaoKinhDoanh , -- TenBaoCaoKinhDoanh - nvarchar(300)
                  @NgayBatDau , -- ThoiGianBatDau - datetime
                  @NgayKetThuc , -- ThoiGianKetThuc - datetime
                  @NguoiLap , -- NguoiLap - nvarchar(100)
                  GETDATE() , -- NgayLap - datetime
                  0 , -- TrangThaiPheDuyet - int
                  NULL , -- NguoiPheDuyet - nvarchar(100)
                  NULL , -- NgayPheDuyet - datetime
                  @NguoiLap , -- CreatedBy - nvarchar(100)
                  GETDATE() , -- CreatedAt - datetime
                  @NguoiLap , -- LastModifiedBy - nvarchar(100)
                  GETDATE() , -- LastModifiedAt - datetime
                  0 , -- DeleteStatus - int
                  0 , -- PrintStatus - int
                  0  -- RecordStatus - int
	          )
	PRINT CONVERT(TIME,GETDATE()) 
	PRINT '1'       
        SELECT  @BPTC_ThongTinBCKDID = MAX(BPTC_ThongTinBCKDID)
        FROM    dbo.BPTC_ThongTinBCKD
        PRINT '2'   
        SELECT @BPTC_TenBaoCao= TenBaoCaoKinhDoanh FROM dbo.BPTC_ThongTinBCKD bttb WHERE bttb.BPTC_ThongTinBCKDID=@BPTC_ThongTinBCKDID
	PRINT CONVERT(TIME,GETDATE())
	PRINT '3'   	        			
		--INSERT DU LIEU VAO CAC TABLE LIEN QUAN
		DECLARE @SQLString nvarchar(500);
		DECLARE @ParmDefinition nvarchar(500);
		
		--BPTC_ThongTinBCKD_BoPhan
		PRINT CONVERT(TIME,GETDATE())
		PRINT '4'   
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_BoPhan @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID,@TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,		
						@TenBaoCao=@BPTC_TenBaoCao;
						
		--BPTC_ThongTinBCKD_BoPhan_DanhSoHaiDau
		PRINT CONVERT(TIME,GETDATE())
		PRINT '5'   
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_BoPhan_DanhSoHaiDau @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID,@TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao=@BPTC_TenBaoCao;		
		
		--BPTC_ThongTinBCKD_Khoi
		PRINT CONVERT(TIME,GETDATE())
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_Khoi @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID,@TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao=@BPTC_TenBaoCao;
					  		
		--BPTC_ThongTinBCKD_Khoi_DanhSo
		PRINT CONVERT(TIME,GETDATE())
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_Khoi_DanhSo @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
					  		
		--BPTC_ThongTinBCKD_Khoi_HoaDon
		PRINT CONVERT(TIME,GETDATE())
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_Khoi_HoaDon @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_ThongTinBCKD_Khoi_ThucChay
		PRINT CONVERT(TIME,GETDATE())
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_Khoi_ThucChay @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_ThongTinBCKD_SanPham		
			PRINT CONVERT(TIME,GETDATE())
				SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_SanPham @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_Get_ThongTinBCKD_XuatHoaDon
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_XuatHoaDon @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_Get_ThongTinBCKD_XuatHoaDon_Nam
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_XuatHoaDon_Nam @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_Get_ThongTinBCKD_XuatHoaDon_ThucChay
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_XuatHoaDon_ThucChay @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_Get_ThongTinBCKD_Huy_ThayDoi
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_Huy_ThayDoi @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_Get_ThongTinBCKD_Huy_ThayDoi_HopDong
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_Huy_ThayDoi_HopDong @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--BPTC_Get_ThongTinBCKD_Huy_ThayDoi_HopDong_Bro
		SET @SQLString = N'exec dbo.BPTC_Get_ThongTinBCKD_Huy_ThayDoi_HopDong_Bro @NgayBatDau, @NgayKetThuc, @ThongTinBCKDID, @TenBaoCao';
		SET @ParmDefinition = N'@ThongTinBCKDID INT,@NgayBatDau DATETIME, @NgayKetThuc DATETIME,@TenBaoCao nvarchar(100)';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @NgayBatDau = @NgayBatDau,
					  @NgayKetThuc = @NgayKetThuc,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID,
					  @TenBaoCao= @BPTC_TenBaoCao;
		--EXEC BPTC_Report_BCKD DE TRA VE DU LIEU LUON
		PRINT CONVERT(TIME,GETDATE())
		/*
		SET @SQLString = N'exec BPTC_Report_BCKD @ThongTinBCKDID';
		SET @ParmDefinition = N'@ThongTinBCKDID INT';
		/* Execute the string with the first parameter value. */
		EXECUTE sp_executesql @SQLString, @ParmDefinition,
					  @ThongTinBCKDID = @BPTC_ThongTinBCKDID;
		*/
		
		SELECT @BPTC_ThongTinBCKDID AS BaoCaoKinhDoanhID		
		
		PRINT CONVERT(TIME,GETDATE())			 
			
    END




```
