# Stored Procedure: `ThucChayDaTinhAdmarket_InsertThucChayNoContract_doannv`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-20 10:13:37.077000
- **Ngày sửa cuối**: 2015-06-20 10:13:37.077000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@TaiKhoan` | `nvarchar(100)` | No |
| `@DmSanPhamREFin` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-07-15
-- Description:	Insert ThucChayDaTinhAdmarket No Contract by day
-- =============================================
/*
	EXEC dbo.ThucChayDaTinhAdmarket_InsertThucChayNoContract '2015-03-11'
*/

CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract_doannv] 
	@NgayThucHien	DATETIME,
	@TaiKhoan NVARCHAR(50),
	@DmSanPhamREFin int
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
			@ThanhTienThucChay		FLOAT			= 0,
			@ThanhTienThucChayKM	FLOAT			= 0,
			@IsNoiBo				INT				= 0,
			@DonViTinh				NVARCHAR(50)	= '',
			@DmMaHopDongREF			INT				= 0,
			@TenMaHopDong			NVARCHAR(50)	= '',
			@DmViTriREF				INT				= 1,
			@TenViTri				NVARCHAR(50)	= ''
			
	DECLARE @SoLuongThucChayNBHopDong	INT		= 0,
			@SoLuongThucChayHopDong		INT		= 0,
			@SoLuongThucChayKMHopDong	INT		= 0,
			@ThanhTienThucChayNBHopDong	FLOAT	= 0,
			@ThanhTienThucChayHopDong	FLOAT	= 0,
			@ThanhTienThucChayKMHopDong	FLOAT	= 0,
			
			@SoLuongThucChayNotHopDong		INT		= 0,
			@SoLuongThucChayKMNotHopDong	INT		= 0,
			@ThanhTienThucChayNotHopDong	FLOAT	= 0,
			@ThanhTienThucChayKMNotHopDong	FLOAT	= 0
			
	--set @NgayThucHien = '2014-12-31'
   
    BEGIN
    	DECLARE product_td CURSOR FOR
    	
    	SELECT  
			tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, 
			CASE tcdt.DonViTinh
				WHEN 'CPC' THEN 'CLICK'
				WHEN 'CPM' THEN 'VIEW'
				ELSE tcdt.DonViTinh
			END AS DonViTinh,
			ISNULL(SUM(tcdt.SoLuongThucChay),0) AS SoLuongThucChay,
			ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay),0) ThanhTienThucChay,
			ISNULL(SUM(tcdt.SoLuongThucChayKM),0) AS SoLuongThucChayKM,
			ISNULL(SUM(tcdt.ThanhTienKM),0) AS ThanhTienThucChayKM,
			CASE WHEN tcdt.DmSanPhamREF IN (144, 299, 337, 628) THEN 1
				 ELSE tcdt.DmViTriREF
			END DmViTriREF, 
			CASE WHEN tcdt.DmSanPhamREF IN (144, 299, 337, 628) THEN ''
				 ELSE tcdt.TenViTri
			END TenViTri
		FROM ThucChayDaTinh AS tcdt 
		WHERE tcdt.NgayThucHien = @NgayThucHien
			AND tcdt.DmSanPhamREF =@DmSanPhamREFin
		GROUP BY
			tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.DonViTinh, tcdt.DmViTriREF, tcdt.TenViTri
    		
    	OPEN product_td;
    	
    	FETCH NEXT FROM product_td INTO @DmSanPhamREF, @TenSanPham, @DmMaHopDongREF, @TenMaHopDong, @DonViTinh,
    									@SoLuongThucChay, @ThanhTienThucChay,
    									@SoLuongThucChayKM, @ThanhTienThucChayKM,
    									@DmViTriREF, @TenViTri
    	
    	WHILE @@FETCH_STATUS = 0
    	BEGIN
    		PRINT 'MA Hop Dong: ' + CONVERT(NVARCHAR(50), @DmMaHopDongREF);
    		
    		PRINT '@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
			PRINT '@SoLuongThucChayKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKM);
			PRINT '@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);
			PRINT '@ThanhTienThucChayKM: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayKM);
			
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
					SELECT  
						tcdt.DmSanPhamREF, tcdt.TenSanPham, 
						CASE tcdt.DmMaHopDongREF 
							WHEN 533 THEN 310
							WHEN 310 THEN 310
							ELSE 0
						END AS DmMaHopDongREF, 
						CASE tcdt.DmMaHopDongREF 
							WHEN 533 THEN 'NB'
							WHEN 310 THEN 'NB'
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
						--AND tcdt.DonViTinh = 'CLICK'
					GROUP BY
						tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.DonViTinh
				)B
				WHERE B.DmMaHopDongREF = @DmMaHopDongREF
			)A 
			PRINT 'DmViTriREF: ' + CONVERT(NVARCHAR(50), @DmViTriREF)		
			
			PRINT '@DonViTinh: ' + CONVERT(NVARCHAR(50), @DonViTinh);
			PRINT '@SoLuongThucChayHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayHopDong);
			PRINT '@SoLuongThucChayKMHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKMHopDong);
			PRINT '@ThanhTienThucChayHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayHopDong);
			PRINT '@ThanhTienThucChayKMHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayKMHopDong);	
						
				
			-- inset to ThucChayDaTinhAdmarket Khach hang
			SET @SoLuongThucChayNotHopDong		= (@SoLuongThucChay - @SoLuongThucChayHopDong);
			SET @SoLuongThucChayKMNotHopDong	= (@SoLuongThucChayKM - @SoLuongThucChayKMHopDong);
			SET @ThanhTienThucChayNotHopDong	= (@ThanhTienThucChay - @ThanhTienThucChayHopDong);
			SET @ThanhTienThucChayKMNotHopDong	= (@ThanhTienThucChayKM - @ThanhTienThucChayKMHopDong);
			
			PRINT '@@SoLuongThucChayNotHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayNotHopDong);
			PRINT '@@SoLuongThucChayKMNotHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKMNotHopDong);
			PRINT '@@ThanhTienThucChayNotHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayNotHopDong);
			PRINT '@@ThanhTienThucChayKMNotHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayKMNotHopDong);	
			IF(@SoLuongThucChayNotHopDong > 0 OR @SoLuongThucChayKMNotHopDong > 0 OR @ThanhTienThucChayNotHopDong > 0 OR @ThanhTienThucChayKMNotHopDong > 0) 
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
					,@TenViTri
			
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
