# Stored Procedure: `Insert_Loai_Treo_DmSanPham_2_CauHinhNhomTinhDoanhSoThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-09-09 15:14:00.573000
- **Ngày sửa cuối**: 2025-09-09 15:27:03.063000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Insert_Loai_Treo_DmSanPham_2_CauHinhNhomTinhDoanhSoThucChay] 
	
AS
BEGIN
	DECLARE @NgayThucHien DATETIME = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
	PRINT @NgayThucHien
	/*HAIDH COMMNET 09/09/2025
	--Thuc hien cap nhap Loai_Treo = 3 tuc la tinh theo kieu chi phi cho table dbo.CauHinhNhomTinhDoanhSoThucChay khi phat sinh san pham moi
	--viec nay duoc thuc hien tu ngày 10/09/2025
	*/
	--1. XAC DINH DANH SACH SAN PHAM CAP NHAP SANG KIEU TREO LA CHI PHI (LOAI_TREO = 3) VA SE TINH THEO KIEU CHI PHI MA CHUA DUOC GHI NHAN
	IF(EXISTS(SELECT s.DmSanPhamID FROM dbo.DmSanPham s
				WHERE s.LastModifiedAt >= @NgayThucHien
				AND s.DeletedStatus = 0
				AND s.Loai_Treo = 3
				AND NOT EXISTS(SELECT TOP (1) c.DmSanPhamREF FROM dbo.CauHinhNhomTinhDoanhSoThucChay c 
								WHERE c.DmSanPhamREF = s.DmSanPhamID 
								AND c.NhomTinhDoanhSoThucChay = 1 
								AND c.DeletedStatus = 0
								)
			)
	)
	BEGIN
		PRINT 'THUC HIEN'
		INSERT INTO [dbo].[CauHinhNhomTinhDoanhSoThucChay]
           ([DmSanPhamREF]
           ,[TenSanPham]
           ,[NhomTinhDoanhSoThucChay]
           ,[ThongtinJobChay]
           ,[DeletedStatus]
           ,[RecordStatus]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy])

		SELECT s.DmSanPhamID ,
			s.TenSanPham,
			1 AS [NhomTinhDoanhSoThucChay],
			N'ThucChay_TinhChiPhiKhac_ByJobs -> sp_TC_InsertThucChayDaTinh_ChiPhiKhac' AS [ThongtinJobChay],
			0 [DeletedStatus],
            0 [RecordStatus],
            GETDATE() [CreatedAt],
            N'JOBS' [CreatedBy],
            GETDATE() [LastModifiedAt],
            N'JOBS' [LastModifiedBy]
		FROM dbo.DmSanPham s
				WHERE s.LastModifiedAt >= @NgayThucHien
				AND s.DeletedStatus = 0
				AND s.Loai_Treo = 3
				AND NOT EXISTS(SELECT TOP (1) c.DmSanPhamREF FROM dbo.CauHinhNhomTinhDoanhSoThucChay c 
								WHERE c.DmSanPhamREF = s.DmSanPhamID 
								AND c.NhomTinhDoanhSoThucChay = 1 
								AND c.DeletedStatus = 0
								)
	END
END




```
