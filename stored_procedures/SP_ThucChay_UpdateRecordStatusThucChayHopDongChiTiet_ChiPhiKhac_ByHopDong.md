# Stored Procedure: `ThucChay_UpdateRecordStatusThucChayHopDongChiTiet_ChiPhiKhac_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-06 16:49:20.743000
- **Ngày sửa cuối**: 2017-07-06 16:49:20.743000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--exec [ThucChay_UpdateThucChayHopDongChiTiet_ChiPhiKhac] '2016-06-28'
CREATE PROCEDURE [dbo].[ThucChay_UpdateRecordStatusThucChayHopDongChiTiet_ChiPhiKhac_ByHopDong]
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50)
AS

BEGIN
	DECLARE @v_str_thuctreocpk NVARCHAR(MAX)
	DECLARE @HDID INT
	SELECT @HDID = HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong

	DECLARE @NgayGioiHanTinh DATETIME
	SET @NgayGioiHanTinh = '2013-01-01'
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
			--AND hdct.HopDongChiTietID =94967
			AND CONVERT(DATE,tt.ThoiGianBatDau) >= @NgayGioiHanTinh
			AND hdct.HopDongFK = @HDID
			AND hdct.DmSanPhamREF IN 
			
			(--- NHOM SP TMDT --------------
							  242 -- Luot up
							  ,241 -- Tin vip												
						--NHOM SP Chi phí--
							, 251 --Thiết kế, quản lý
							, 252 --Hosting
							, 253 --Chi phi khac									
							, 535 --Chi phí quản lý campaign
							, 537 --Chi phí viết bài
							, 538 --Chi phí thiết kế
							, 539 --Chi phí dựng clip
							, 540 --Chi phí sáng tạo
							, 541 --Chi phí giải thưởng cuộc thi/ Contest
							, 542 --Chi phí xây dưng microsite/ tab
							, 555 --Chi phí trài trợ
							, 556 --Hiệu đính
							, 557 --Chèn Clip
							, 558 --Chi phí viết bài
							, 559 --Chi phí quay clip
							, 560 --Chi phí sản xuất										
							, 561 -- Chi phí khảo sát thị trường online
							--bo sung
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding
							,631 -- Facebook Seeding
							, 651 -- Đăng tin fanpage
							,726	--Tư vấn viết đề án truyền thông
							,731	--KOL
							,730	--livestream
							,633
							,629
							,729
							,736 -- Chi phí công nghệ
						)
			for xml path('') 
		), 1, 1, '') AS DotChayBooking
	)
	SELECT @v_str_thuctreocpk
	
	UPDATE ThucChayHopDongChiTiet
	SET RecordStatus = 1 
	WHERE ThucChayHopDongChiTietID IN (SELECT att.item FROM dbo.ArrayToTable(dbo.Array(@v_str_thuctreocpk, ',') ) att)

END

	

--endregion


```
