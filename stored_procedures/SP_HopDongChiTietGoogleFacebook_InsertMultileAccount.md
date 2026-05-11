# Stored Procedure: `HopDongChiTietGoogleFacebook_InsertMultileAccount`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:22.623000
- **Ngày sửa cuối**: 2015-05-25 11:34:32.647000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.HopDongChiTietGoogleFacebook_InsertMultileAccount '2014-12-31'
*/
CREATE PROCEDURE [dbo].[HopDongChiTietGoogleFacebook_InsertMultileAccount]
	-- Add the parameters for the stored procedure here
	@ngayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @phanBoId	INT,
			@accountPhanBo	NVARCHAR(512),
			@account	NVARCHAR(50)
			
	-- Delete truoc khi insert du lieu moi nhat cho den ngay tinh thuc chay		
	TRUNCATE TABLE 	HopDongChiTietGoogleFacebook;
			
	DECLARE pb_cursor CURSOR FOR
	SELECT HopDongChiTietID, TK_Admarket 
	FROM HopDongChiTiet A
	WHERE A.DeletedStatus = 0
		AND DmSanPhamREF in (306,423)
		AND A.CreatedAt >= '2014-01-01'
		AND CHARINDEX(',', A.TK_Admarket) > 0
		AND CONVERT(DATE,A.CreatedAt) <= @ngayThucHien
		--AND A.HopDongChiTietID = 66397
	
	OPEN pb_cursor;
	
	FETCH NEXT FROM pb_cursor INTO @phanBoId, @accountPhanBo
	
	WHILE @@FETCH_STATUS = 0
	BEGIN	
		SELECT @phanBoId, @accountPhanBo;
		
		DECLARE acc_cursor CURSOR FOR
		SELECT Items FROM [dbo].StringSplitter(@accountPhanBo,',')
		
		OPEN acc_cursor;
		
		FETCH NEXT FROM acc_cursor INTO @account
		WHILE @@FETCH_STATUS = 0
		BEGIN
			INSERT INTO HopDongChiTietGoogleFacebook
			SELECT [HopDongChiTietID]
				  ,[HopDongFK]
				  ,[DanhSachNhanHangREF]
				  ,[NhanHang]
				  ,[DmNhomNganhREF]
				  ,[TenNhomNganh]
				  ,[DmLoaiREF]
				  ,[TenLoai]
				  ,[DmNhomWebsiteREF]
				  ,[TenNhomWebsite]
				  ,[DmWebsiteREF]
				  ,[TenWebsite]
				  ,[DmSanPhamREF]
				  ,[TenSanPham]
				  ,[DmLoaiBannerREF]
				  ,[TenLoaiBanner]
				  ,[DmChuyenMucREF]
				  ,[TenChuyenMuc]
				  ,[DmViTriREF]
				  ,[TenViTri]
				  ,[ThoiGian]
				  ,[SoLuong]
				  ,[DonViTinhREF]
				  ,[DonViTinh]
				  ,[DonGia]
				  ,[ChietKhau]
				  ,[GiamGia]
				  ,[TiLeTuVan]
				  ,[KhuyenMai]
				  ,[IsKhuyenMai]
				  ,[ChiPhiTuVan]
				  ,[ThanhTien]
				  ,[GhiChu]
				  ,[CreatedBy]
				  ,[CreatedAt]
				  ,[LastModifiedBy]
				  ,[LastModifiedAt]
				  ,[DeletedStatus]
				  ,[PrintStatus]
				  ,[RecordStatus]
				  ,[DmSanphamREF_old]
				  ,dbo.TRIM(@account) TK_Admarket
				  ,[TK_AdMarketID]
				  ,[SoluongThucChay]
				  ,[ThanhtienThucChay]
				  ,[TrangthaiThucChay]
				  ,[ThoiGianBatDau]
				  ,[ThoiGianKetThuc]
				  ,[ThucChayDenNgay]
				  ,[DmBannerREF]
				  ,[TenBanner]
			  FROM [HopDongChiTiet] 
			  WHERE HopDongChiTietID = @phanBoId
			
			FETCH NEXT FROM acc_cursor INTO @account
		END
		
		CLOSE acc_cursor;
		DEALLOCATE acc_cursor;
		
		FETCH NEXT FROM pb_cursor INTO @phanBoId, @accountPhanBo
	END
	
	CLOSE pb_cursor;
	DEALLOCATE pb_cursor;
END

```
