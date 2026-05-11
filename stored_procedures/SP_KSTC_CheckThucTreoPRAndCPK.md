# Stored Procedure: `KSTC_CheckThucTreoPRAndCPK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 17:17:24.337000
- **Ngày sửa cuối**: 2014-12-08 17:17:24.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckThucTreoPRAndCPK 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT
AS
BEGIN
IF @DmSanPhamREF = 141
BEGIN
	SELECT distinct HopDongREF, HopDongChiTietREF FROM (							
	SELECT tc.ThoiGianBatDau, tc.ThucChayHopDongChiTietPRID, tc.HopDongREF,tc.HopDongChiTietREF, tc.createdat,tc.LastModifiedAt							
		FROM dbo.ThucChayHopDongChiTietPR tc						
		 WHERE tc.DeletedStatus <> 1 						
		 AND tc.RecordStatus = 0						
		 AND tc.HopDongChiTietREF <> 0						
		 AND tc.HopDongREF NOT IN (SELECT HopDongID FROM HOpDong WHERE HOpDong.TrangThaiHopDong = 3)						
		AND tc.ThoiGianBatDau >='2013-01-01'						
		AND tc.ThucChayHopDongChiTietPRID NOT IN (13337) -- phan bo năm 2013 chưa tính thực chạy						
	AND convert(Date,tc.CreatedAt )<= @NgayThucHien			
	)a				
END
ELSE 
BEGIN						
--Chi phí khác							
SELECT tc.ThucChayHopDongChiTietID,tc.Hopdongref, tc.HopDongChiTietREF, ct.DmSanPhamREF, tc.CreatedAt, tc.LastModifiedAt							
  FROM ThucChayHopDongChiTiet tc							
INNER JOIN HopDongChiTiet ct ON ct.HopDongChiTietID = tc.HopDongChiTietREF							
WHERE ct.DmSanPhamREF IN 							
					(--- NHOM SP TMDT --------------		
							  242 -- Luot up
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
						)	
AND tc.ThoiGianBatDau>='2013-01-01' 							
AND tc.ThucChayHopDongChiTietID NOT IN (25375,24688)							
AND tc.HopDongREF NOT IN (SELECT HopDongID FROM hopdong WHERE hopdong.TrangThaiHopDong = 3)							
	  AND tc.HopDongREF NOT IN (SELECT HopDongFK FROM HopDongChiTiet WHERE DmSanPhamREF IN (306,423))						
AND ct.DeletedStatus <> 1							
AND tc.DeletedStatus <> 1							
AND tc.RecordStatus = 0							
AND convert(Date,tc.CreatedAt )<= @NgayThucHien							
ORDER BY ct.DmSanPhamREF							
END	
END

```
