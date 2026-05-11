# Stored Procedure: `ThucChay_UpdateThucChayHopDongChiTiet_ChiPhi_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 16:14:27.357000
- **Ngày sửa cuối**: 2017-03-16 15:54:35.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--exec [ThucChay_UpdateThucChayHopDongChiTiet_ChiPhiKhac] '2014-06-19'
CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayHopDongChiTiet_ChiPhi_SanPhamChinh]
	@NgayThucHien datetime
AS

BEGIN
	DECLARE @NgayGioiHanTinh DATETIME
	SET @NgayGioiHanTinh ='2013-01-01'
	DECLARE @v_str_thuctreocpk NVARCHAR(MAX)
	SET @v_str_thuctreocpk = 
	(SELECT
		stuff(
		(
			SELECT cast(',' as varchar(max)) + Convert(nvarchar(20),ThucChayHopDongChiTietID)
			  FROM ThucChayHopDongChiTiet tt
			  INNER JOIN HopDongChiTiet hdct ON tt.HopDongChiTietREF = hdct.HopDongChiTietID 
			WHERE (CASE when tt.CreatedAt >= tt.LastModifiedAt THEN Convert(date,tt.CreatedAt) 
			else Convert(date,tt.LastModifiedAt)
			END
			)  = @NgayThucHien
			AND tt.RecordStatus = 0
			AND tt.HopDongChiTietREF <> 0 
			AND hdct.DmSanPhamREF IN (140,228,549,564,375,231,238,337,531,370,339,342,381,680)
			AND hdct.DmLoaiBannerREF = 17 --Chi Phi cho san pham chinh
			AND CONVERT(DATE,tt.ThoiGianBatDau) >=  @NgayGioiHanTinh
			for xml path('') 
		), 1, 1, '') AS DotChayBooking
	)
	
	UPDATE ThucChayHopDongChiTiet
	SET RecordStatus = 1 
	WHERE ThucChayHopDongChiTietID IN (SELECT att.item FROM dbo.ArrayToTable(dbo.Array(@v_str_thuctreocpk, ',') ) att)

END

	

--endregion

```
