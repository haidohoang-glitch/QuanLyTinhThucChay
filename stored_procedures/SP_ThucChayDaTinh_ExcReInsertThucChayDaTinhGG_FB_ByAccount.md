# Stored Procedure: `ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_ByAccount`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-06 10:28:51.270000
- **Ngày sửa cuối**: 2015-04-22 12:26:42.010000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |
| `@account` | `nvarchar(510)` | No |
| `@sanPhamId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_ByAccount 
		'2015-04-20', 
		'Vietjet_Dai Loan',
		423
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ExcReInsertThucChayDaTinhGG_FB_ByAccount]
	-- Add the parameters for the stored procedure here
	@ngayThucHien	DATETIME,
	@account	NVARCHAR(255),
	@sanPhamId	INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE 
			@type			NVARCHAR(50)		
	
	--WHILE @ngayThucHien <= @endDate
	BEGIN
		
		--EXEC dbo.ThucChayGoogleFacebookByDay_InsertDataByDayAccount @ngayThucHien, @account
		
		-- Run manual
		TRUNCATE TABLE ThucChayGoogleFacebookByDay
    
		INSERT INTO ThucChayGoogleFacebookByDay
		SELECT 
			DmSanPhamREF,
			TenSanPham,
			TaiKhoan,
			SUM(SoNgayChay) SoNgayChay,
			SUM(Click) Click,
			SUM(ThanhTien) ThanhTien,
			[Type],
			NEWID() ThucChayGoogleFacebookID,
			@ngayThucHien NgayThucHien,
			GETDATE() CreatedAt,
			'asd' CreatedBy,
			GETDATE() LastModifiedAt,
			'asd' LastModifiedBy,
			0 RecordStatus,
			DeletedStatus
		FROM ThucChayGoogleFacebook A
		WHERE 1 = 1 
			AND A.NgayThucHien = @ngayThucHien
			--AND A.NgayThucHien <= '2015-03-04'
			AND A.RecordStatus = 1
			AND A.TaiKhoan = @account
		GROUP BY
			DmSanPhamREF,
			TenSanPham,
			TaiKhoan,
			[Type],
			DeletedStatus	
			
		DECLARE acc_cursor CURSOR FOR
		SELECT DISTINCT
			A.NgayThucHien, A.TaiKhoan, A.DmSanPhamREF, A.[Type]
		FROM	ThucChayGoogleFacebookByDay A
		WHERE 1=1
			AND A.NgayThucHien = @ngayThucHien
			AND A.TaiKhoan = @account
		
		OPEN acc_cursor
		
		FETCH NEXT FROM acc_cursor INTO @ngayThucHien, @account, @sanPhamId, @type
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			SELECT @ngayThucHien, @account, @sanPhamId, @type
			
			-- Update status trong bang online
			UPDATE ThucChayGoogleFacebookOnline
			SET RecordStatus = 1,
				LastModifiedAt = GETDATE()
			WHERE TaiKhoan = @account
				AND DmSanPhamREF = @sanPhamId
				AND [Type] = @type
			
			EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhGG_FB 
				@ngayThucHien, 
				@account, 
				@sanPhamId,
				@type
			
			FETCH NEXT FROM acc_cursor INTO @ngayThucHien, @account, @sanPhamId, @type
		END
		
		CLOSE acc_cursor
		DEALLOCATE acc_cursor
		
		-- Update gia tri thay doi
		
		--EXEC dbo.ThucChayDaTinh_GG_FB_UpdateGiaTriThayDoi @ngayThucHien
		
		--SET @ngayThucHien = DATEADD(d, 1, @ngayThucHien);
	END
    
END

```
