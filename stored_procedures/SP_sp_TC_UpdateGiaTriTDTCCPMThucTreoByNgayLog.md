# Stored Procedure: `sp_TC_UpdateGiaTriTDTCCPMThucTreoByNgayLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 16:29:55.303000
- **Ngày sửa cuối**: 2024-09-26 15:41:59.590000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@CONTENT_LOG` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_TC_UpdateGiaTriTDTCCPMThucTreoByNgayLog] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongREF INT,
	@DmSanPhamID INT,
	@HopDongChiTietREF INT,
	@CONTENT_LOG NVARCHAR(500)
AS
BEGIN
	DECLARE @MinDate DATETIME,
	        @SoLuongLechTreoHa BIGINT,
	        @SoLuongThucChayDuocTinh BIGINT,
			@v_SoHopDong NVARCHAR(100) = ''
	
	DECLARE @SoLuongThucChay BIGINT,
	        @SoLuongHopDong BIGINT,
	        @TTChenhLechDuocTinh FLOAT
	
	DECLARE @count_HDCT              INT,
	        @DonGiaTheoDonViTinh     FLOAT,
	        @TTThucChaySauChietKhau  FLOAT,
	        @GiaTriThayDoi           FLOAT,
	        @TongTienThucChay		 FLOAT,
	        @TongTienHopDong		BIGINT,
	        @IsHDFinish				INT
	
	SET @TongTienHopDong = 0
	SET @IsHDFinish = 0
	SET @count_HDCT = 0
	SET @SoLuongLechTreoHa = 0
	SET @SoLuongThucChayDuocTinh = 0
	SET @SoLuongThucChay = 0
	SET @SoLuongHopDong = 0
	SET @DonGiaTheoDonViTinh = 0
	SET @TTThucChaySauChietKhau = 0
	SET @GiaTriThayDoi = 0
	SET @TTChenhLechDuocTinh = 0
	SET @TongTienThucChay = 0
	
	IF (@count_HDCT = 0)--T/c tinh theo phuong phap thuc treo
	BEGIN
	    SET @MinDate = (
	            SELECT MIN(tcdt.NgayThucHien)
	            FROM   dbo.ThucChayDaTinh tcdt
	            WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	                   AND tcdt.DmSanPhamREF = @DmSanPhamID
	                   AND tcdt.HopDongID = @HopDongREF
	        )
	    
	    SET @MinDate = ISNULL(@MinDate, GETDATE())
	    IF (CONVERT(date, @MinDate) < CONVERT(date, @NgayThucHien))
	    BEGIN
	        --Tinh s/l thuc chay 
	        SET @SoLuongThucChay = (
	                SELECT SUM(tcdt.SoLuongThucChay)
	                FROM   dbo.ThucChayDaTinh tcdt
	                WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	                       AND tcdt.DmSanPhamREF = @DmSanPhamID
	                       AND tcdt.HopDongID = @HopDongREF
	                       AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
	            )
	        
	        SET @SoLuongThucChay = ISNULL(@SoLuongThucChay, 0)
	        --Tinh s/l HopDong
	        SET @SoLuongHopDong = (
	                SELECT hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                FROM   dbo.HopDongChiTiet hdct
	                WHERE  hdct.HopDongChiTietID = @HopDongChiTietREF
	                       AND hdct.DeletedStatus = 0
	            )
	        --Tinh DonGiaTheoDonViTinh sau chiet khau
	        SET @DonGiaTheoDonViTinh = (
	                SELECT (
	                           hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                       ) * (100 -hdct.ChietKhau) / 100
	                FROM   dbo.HopDongChiTiet hdct
	                WHERE  hdct.HopDongChiTietID = @HopDongChiTietREF
	                       AND hdct.DmSanPhamREF = @DmSanPhamID
	                       AND hdct.DeletedStatus = 0
	            )
	        
	        SET @DonGiaTheoDonViTinh = ISNULL(@DonGiaTheoDonViTinh, 0)
	        
	        --Tinh Tong tien t/c sau chiet khau, Gia tri thay doi
	        SELECT @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay),
	               @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi),
				   @v_SoHopDong = tcdt.SoHopDong
	        FROM   dbo.ThucChayDaTinh tcdt
	        WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	               AND tcdt.DmSanPhamREF = @DmSanPhamID
	               AND tcdt.HopDongID = @HopDongREF
	               AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien	
			GROUP BY tcdt.SoHopDong
	        
	        SET @TTThucChaySauChietKhau = ISNULL(@TTThucChaySauChietKhau, 0)
	        SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi, 0)
	        
	        --CHECK TINH S./L THUCCHAY DUOC TINH
	        IF (
	               @SoLuongThucChay > 0
	               AND @SoLuongThucChay < @SoLuongHopDong
	           )
	        BEGIN
	            --Tinh s/l LechTreoHa
	            SET @SoLuongLechTreoHa = (
	                    SELECT SUM(tcdt.SoLuongThucChayLechTreoHa)
	                    FROM   dbo.ThucChayDaTinh tcdt
	                    WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	                           AND tcdt.DmSanPhamREF = @DmSanPhamID
	                           AND tcdt.HopDongID = @HopDongREF
	                           AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
	                )
	            
	            SET @SoLuongLechTreoHa = ISNULL(@SoLuongLechTreoHa, 0)
	            IF (
	                   (@SoLuongLechTreoHa > 0)
	                   AND (@SoLuongThucChay + @SoLuongLechTreoHa <= @SoLuongHopDong)
	               )
	            BEGIN
	                SET @SoLuongThucChayDuocTinh = @SoLuongThucChay + @SoLuongLechTreoHa
	            END
	            ELSE 
	            IF (
	                   (@SoLuongLechTreoHa > 0)
	                   AND (@SoLuongThucChay + @SoLuongLechTreoHa > @SoLuongHopDong)
	               )
	            BEGIN
	                SET @SoLuongThucChayDuocTinh = (@SoLuongThucChay + @SoLuongLechTreoHa) 
	                    -((@SoLuongThucChay + @SoLuongLechTreoHa) - @SoLuongHopDong)
	            END
	            ELSE 
	            IF (@SoLuongLechTreoHa <= 0)
	            BEGIN
	                SET @SoLuongThucChayDuocTinh = @SoLuongThucChay
	            END
	            SET @TTChenhLechDuocTinh = (@SoLuongThucChayDuocTinh * @DonGiaTheoDonViTinh)
	            -(@TTThucChaySauChietKhau + @GiaTriThayDoi)
	        END
	        --
	        --   
			IF (@SoLuongThucChay >= @SoLuongHopDong)
			BEGIN
				SET @isHDFinish = 1
				SET @TongTienHopDong =
				(
					SELECT sum(hdct.ThanhTien)
					FROM   dbo.HopDongChiTiet hdct
					WHERE  hdct.HopDongFK = @HopDongREF
						   AND hdct.HopDongChiTietID = @HopDongChiTietREF
						   AND hdct.DmSanPhamREF = @DmSanPhamID
						   AND hdct.DeletedStatus = 0
						   AND hdct.ChietKhau <> 100
				)           
				SET @TTChenhLechDuocTinh  =  @TongTienHopDong  -(@TTThucChaySauChietKhau + @GiaTriThayDoi)
				SET @IsHDFinish = 1
			END

	        IF(@TTThucChaySauChietKhau + @GiaTriThayDoi = 0)
				SET @TongTienThucChay = @TTChenhLechDuocTinh
			ELSE
				SET @TongTienThucChay = @TTThucChaySauChietKhau + @GiaTriThayDoi
	        IF(@TongTienThucChay = 0)
				SET @TongTienThucChay = 1
				
	        --PRINT 'Thanh tien chenh lech :' + CONVERT(NVARCHAR(50), @TTChenhLechDuocTinh)    
			--PRINT @HopDongChiTietREF	        
	        IF (@TTChenhLechDuocTinh <> 0)
	        BEGIN
				--HAIDH COMMENT 26092024 THAY HAM TINH GIA TRI THAY DOI CU BANG HAM TINH MOI
				EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Job_V2]  -- Add the parameters for the stored procedure here
					@dtStart = @MinDate, 
					@dtEnd = @NgayThucHien ,
					@pSoHopDong = @v_SoHopDong ,
					@pHopDongChiTietID = @HopDongChiTietREF,
					@NgayTinh = @NgayThucHien
  
	        END
	    END
	END
	
	SELECT 2
END



```
