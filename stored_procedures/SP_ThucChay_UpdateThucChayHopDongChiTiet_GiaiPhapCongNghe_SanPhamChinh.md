# Stored Procedure: `ThucChay_UpdateThucChayHopDongChiTiet_GiaiPhapCongNghe_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-12 09:45:34.887000
- **Ngày sửa cuối**: 2018-05-02 09:47:30.830000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_TinhChiPhiKhac_ByJobs]
CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayHopDongChiTiet_GiaiPhapCongNghe_SanPhamChinh]
	@NgayThucHien DATETIME
AS
BEGIN
	
	DECLARE @NgayGioiHanTinh DATETIME ='2013-01-01'
	
	UPDATE dbo.ThucChayHopDongChiTiet
	SET RecordStatus = 1
	WHERE ThucChayHopDongChiTietID IN
	(
		SELECT tc.ThucChayHopDongChiTietID FROM 
 		(
 			SELECT * FROM HopDongChiTiet 
 				WHERE DmSanPhamREF in (370,339,342,598,775)
 				AND DeletedStatus = 0 
 				AND (DmLoaiNenTangREF = 8 --Retargeting & Content base
					OR DmSanPhamREF = 775 -- campaing audit
				)
 				AND NOT((HopDongChiTiet.DmLoaiBannerREF IN (18)) OR (HopDongChiTiet.DmLoaiREF = 13))-- --Khong tinh thuc chay cho HTQC Mua Ngoai
 		) C  
 		INNER JOIN  
 		( 
 			SELECT hd.HopDongID FROM dbo.HopDong hd 
 			WHERE hd.TrangThaiHopDong <> 3
 			AND hd.DeletedStatus = 0
 		) D on D.HopDongID = C.HopDongFK
 		INNER JOIN 
		(
			SELECT tchdctp.HopDongChiTietREF,tchdctp.ThucChayHopDongChiTietID FROM dbo.ThucChayHopDongChiTiet tchdctp
			WHERE 1=1
			AND (CASE when CreatedAt >= LastModifiedAt THEN Convert(date,CreatedAt) 
				else Convert(date,LastModifiedAt)
				END
			)   = CONVERT(DATE,@NgayThucHien)
			AND tchdctp.DeletedStatus = 0
			AND tchdctp.RecordStatus = 0
			--AND tchdctp.InputType = 1 --TreoTuDong
			AND Convert(date,tchdctp.ThoiGianBatDau) >= @NgayGioiHanTinh 
		)TC ON c.HopDongChiTietID = tc.HopDongChiTietREF
	)
END

```
