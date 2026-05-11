# Stored Procedure: `KiemTra_ChayXong_ChiPhiKhac_2016`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-29 18:58:03.960000
- **Ngày sửa cuối**: 2016-11-29 18:58:03.960000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROC [KiemTra_ChayXong_ChiPhiKhac_2016]
AS 

BEGIN
SELECT
	TC.SoHopDong,
	TC.TenHTQC,
	TC.DMSanPhamREF,
	TC.[Tên sản phẩm],
	TC.[Tên loại banner ],
	TC.thanhtienhd,
	TC.ThanhTienThucChay,
	TC.ThanhTienThucChay2016,
	TC.[Trang thai chay]
FROM dbo.['ThucChay2016_01012611']  TC

WHERE TC.DmSanPhamREF IN(
							 242 -- Luot up
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
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding	
							,631 -- facebook seeding
							,651 -- đăng tin fanpage
							,726 --Tư vấn viết đề án truyền thông
							,731 --KOL)
						
							)
							
AND TC.DmHinhThucQuangCao NOT IN (22,28,29,30,31,32,33)
AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
AND thanhtienthucchay=thanhtienhd
ORDER BY SoHopDong

END





```
