# Stored Procedure: `ThucChayDaTinhAdmarket_InsertThucChayNoContract`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:54.960000
- **Ngày sửa cuối**: 2024-01-16 17:53:28.217000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: 2017
-- Description:	Insert ThucChayDaTinhAdmarket No Contract by day
-- =============================================
/*
	EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract '2017-04-18'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract] 
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    
    DECLARE @DmSanPhamREF			INT				= 0,
			@TenSanPham				NVARCHAR(255)	= '',
			@SoLuongThucChayNB		INT				= 0,	
			@SoLuongThucChay		INT				= 0,
			@SoLuongThucChayKM		INT				= 0,
			@ThanhTienThucChayNB	FLOAT			= 0,
			@ThanhTienThucChay		money			= 0,
			@ThanhTienThucChayKM	FLOAT			= 0,
			@IsNoiBo				INT				= 0,
			@DonViTinh				NVARCHAR(50)	= '',
			@DmMaHopDongREF			INT				= 0,
			@TenMaHopDong			NVARCHAR(50)	= '',
			@DmViTriREF				INT				= 0,
			@TenViTri				NVARCHAR(50)	= ''
			
	DECLARE @SoLuongThucChayNBHopDong	INT		= 0,
			@SoLuongThucChayHopDong		INT		= 0,
			@SoLuongThucChayKMHopDong	INT		= 0,
			@ThanhTienThucChayNBHopDong	FLOAT	= 0,
			@ThanhTienThucChayHopDong	money	= 0,
			@ThanhTienThucChayKMHopDong	FLOAT	= 0,
			
			@SoLuongThucChayNotHopDong		INT		= 0,
			@SoLuongThucChayKMNotHopDong	INT		= 0,
			@ThanhTienThucChayNotHopDong	money	= 0,
			@ThanhTienThucChayKMNotHopDong	FLOAT	= 0
			
	--set @NgayThucHien = '2014-12-31'
   
    BEGIN
    	DECLARE product_td CURSOR FOR
    	
    	SELECT  
			tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, 
			CASE tcdt.DonViTinh
				WHEN 'CLICK' THEN 'CPC'
				WHEN 'CPM' THEN 'VIEW'
				ELSE tcdt.DonViTinh
			END AS DonViTinh,
			ISNULL(SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi),0) AS SoLuongThucChay,
			ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0) ThanhTienThucChay,
			ISNULL(SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi),0) AS SoLuongThucChayKM,
			ISNULL(SUM(tcdt.ThanhTienKM+ tcdt.GiaTriKMThayDoi),0) AS ThanhTienThucChayKM,
			CASE WHEN tcdt.DmSanPhamREF IN (144, 299, 337, 628) THEN 0
				 ELSE tcdt.DmViTriREF
			END DmViTriREF, 
			CASE WHEN tcdt.DmSanPhamREF IN (144, 299, 337, 628) THEN ''
				 ELSE tcdt.TenViTri
			END TenViTri
		FROM ThucChayDaTinh AS tcdt 
		WHERE tcdt.NgayThucHien = @NgayThucHien
			AND tcdt.DmSanPhamREF IN (144, 299, 337, 585, 628)
			-- Doannv 
			and tcdt.DmHinhThucQuangCao <>42 -- thuongcmt --haidh comment lai ngay 12/12/2022 vi do tinh ca admatic vao thuong
			AND tcdt.DmHinhThucQuangCao <> 13 AND tcdt.DmLoaiBannerREF <> 18
		GROUP BY
			tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.DonViTinh, tcdt.DmViTriREF, tcdt.TenViTri
    		
    	OPEN product_td;
    	
    	FETCH NEXT FROM product_td INTO @DmSanPhamREF, @TenSanPham, @DmMaHopDongREF, @TenMaHopDong, @DonViTinh,
    									@SoLuongThucChay, @ThanhTienThucChay,
    									@SoLuongThucChayKM, @ThanhTienThucChayKM,
    									@DmViTriREF, @TenViTri
    	
    	WHILE @@FETCH_STATUS = 0
    	BEGIN
   -- 		PRINT 'MA Hop Dong: ' + CONVERT(NVARCHAR(50), @DmMaHopDongREF);
    		
   -- 		PRINT '@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
			--PRINT '@SoLuongThucChayKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKM);
			--PRINT '@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);
			--PRINT '@ThanhTienThucChayKM: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayKM);
			
    		-- Select thanh tien co hop dong
    		SELECT 
				@SoLuongThucChayHopDong  = ISNULL(SUM(A.SoLuongThucChay),0),
				@SoLuongThucChayKMHopDong = ISNULL(SUM(A.SoLuongThucChayKM),0),
				@ThanhTienThucChayHopDong = ISNULL(SUM(A.ThanhTienThucChay),0),
				@ThanhTienThucChayKMHopDong = ISNULL(SUM(A.ThanhTienThucChayKM),0)
			FROM
			(
				SELECT B.*
				FROM
				(
				    SELECT C.DmSanPhamREF,C.TenSanPham,C.DmMaHopDongREF,C.TenMaHopDong,C.DonViTinh,
					SUM(SoLuongThucChay) SoLuongThucChay,
					SUM(ThanhTienThucChay) ThanhTienThucChay,
					SUM(SoLuongThucChayKM) SoLuongThucChayKM,
					SUM(ThanhTienThucChayKM) ThanhTienThucChayKM
					FROM
					(
					SELECT  
				
						tcdt.DmSanPhamREF, tcdt.TenSanPham, 
						CASE tcdt.DmMaHopDongREF 
							WHEN 533 THEN 310
							WHEN 310 THEN 310
							WHEN 5151 THEN 310
							WHEN 5152 THEN 310
							WHEN 5153 THEN 310
							WHEN 5154 THEN 310
							ELSE 0
						END AS DmMaHopDongREF, 
						CASE tcdt.DmMaHopDongREF 
							WHEN 533 THEN 'NB' 	--S-NB  5151;--C-NB  5152; --NBNG  5153;--S2-NB	5154
							WHEN 310 THEN 'NB'
							WHEN 5151 THEN 'NB'
							WHEN 5152 THEN 'NB'
							WHEN 5153 THEN 'NB'
							WHEN 5154 THEN 'NB'
							ELSE ''
						END AS TenMaHopDong, 
						tcdt.DonViTinh DonViTinh,
						ISNULL(SUM(tcdt.SoLuongThucChay),0) AS SoLuongThucChay,
						SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)) ThanhTienThucChay,
						ISNULL(SUM(tcdt.SoLuongThucChayKM),0) AS SoLuongThucChayKM,
						ISNULL(SUM(tcdt.ThanhTienKM),0) AS ThanhTienThucChayKM
					FROM ThucChayDaTinhAdmarket AS tcdt 
					WHERE tcdt.NgayThucHien = @NgayThucHien
						AND tcdt.DmSanPhamREF = @DmSanPhamREF
						AND tcdt.DonViTinh = @DonViTinh
						AND tcdt.DmViTriREF = @DmViTriREF
						-- Doannv 
						and tcdt.DmHinhThucQuangCao <> 42 -- thuongcmt --haidh comment lai ngay 12/12/2022 vi do tinh ca admatic vao thuong
						AND tcdt.DmHinhThucQuangCao <> 13 AND tcdt.DmLoaiBannerREF <> 18
						--AND tcdt.DonViTinh = 'CLICK'
					GROUP BY
						tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.DonViTinh
				)C group by C.DmSanPhamREF,C.TenSanPham,C.DmMaHopDongREF,C.TenMaHopDong,C.DonViTinh
				)B
				WHERE B.DmMaHopDongREF = @DmMaHopDongREF
			)A 
			--PRINT 'DmViTriREF: ' + CONVERT(NVARCHAR(50), @DmViTriREF)		
			
			--PRINT '@DonViTinh: ' + CONVERT(NVARCHAR(50), @DonViTinh);
			--PRINT '@SoLuongThucChayHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayHopDong);
			--PRINT '@SoLuongThucChayKMHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKMHopDong);
			--PRINT '@ThanhTienThucChayHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayHopDong);
			--PRINT '@ThanhTienThucChayKMHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayKMHopDong);	
						
				
			-- inset to ThucChayDaTinhAdmarket Khach hang
			SET @SoLuongThucChayNotHopDong		= (@SoLuongThucChay - @SoLuongThucChayHopDong);
			SET @SoLuongThucChayKMNotHopDong	= (@SoLuongThucChayKM - @SoLuongThucChayKMHopDong);
			SET @ThanhTienThucChayNotHopDong	= (@ThanhTienThucChay - @ThanhTienThucChayHopDong);
			SET @ThanhTienThucChayKMNotHopDong	= (@ThanhTienThucChayKM - @ThanhTienThucChayKMHopDong);

			--print @DmMaHopDongREF
			--print @DmSanPhamREF
			--print @DmViTriREF
			--print @DonViTinh
			--print @ThanhTienThucChay
			--print @ThanhTienThucChayHopDong
			--print @ThanhTienThucChayNotHopDong	
			
			IF(@SoLuongThucChayNotHopDong <> 0 OR @SoLuongThucChayKMNotHopDong <> 0 OR @ThanhTienThucChayNotHopDong <> 0 OR @ThanhTienThucChayKMNotHopDong <> 0) 
			BEGIN
				
			--PRINT('doannv')
			declare @tenvitri_new nvarchar(100) = case when @DmSanPhamREF = 144 then N'CPC Admarket' else @TenViTri end
			EXEC dbo.ThucChayDaTinhAdmarket_InsertNoContractByProduct
					@DmSanPhamREF
					,@TenSanPham
					,@DonViTinh
					,0 --DmWebsiteREF
					,'' --@TenWebsite
					,@NgayThucHien
					,@SoLuongThucChayNotHopDong
					,@SoLuongThucChayKMNotHopDong
					,@ThanhTienThucChayNotHopDong
					,@ThanhTienThucChayKMNotHopDong
					,@DmMaHopDongREF
					,@TenMaHopDong								
					,'MuaOnline'
					,0
					,0
					,@DmViTriREF
					,@tenvitri_new
			END
    		FETCH NEXT FROM product_td INTO @DmSanPhamREF, @TenSanPham, @DmMaHopDongREF, @TenMaHopDong, @DonViTinh,
    										@SoLuongThucChay, @ThanhTienThucChay,
    										@SoLuongThucChayKM, @ThanhTienThucChayKM,
    										@DmViTriREF, @TenViTri
    	END
    	
    	CLOSE product_td;
    	DEALLOCATE product_td;
    END
END



```
