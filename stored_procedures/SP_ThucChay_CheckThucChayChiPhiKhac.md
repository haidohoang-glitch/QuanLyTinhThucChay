# Stored Procedure: `ThucChay_CheckThucChayChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-06 17:15:36.977000
- **Ngày sửa cuối**: 2019-01-29 15:32:28.150000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_CheckThucChayChiPhiKhac] '2014-06-05','2014-06-05'
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayChiPhiKhac]
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
			SELECT 
			A.SoHopDong,
			A.HopDongID,
			A.HopDongChiTietREF,
			A.NgayThucHien,
			ISNULL(A.SLChay, 0) AS SLThucChay,
			ISNULL(A.SLKM, 0) AS SLThucChayKM,
			ISNULL(A.DonGia, 0) AS DonGia,
			ISNULL(A.TT ,0) AS ThanhTienThucChay,
			B.HopDongREF,
			B.HopDongChiTietREF,
			ISNULL(B.SoLuong,0) AS SLThucTreo,
			ISNULL(B.TT ,0) AS ThanhTienThucTreo,
			(ISNULL(A.SLChay, 0) + ISNULL(A.SLKM, 0) - ISNULL(B.SoLuong,0)) AS SLLech,
			ISNULL(A.TT ,0) - ISNULL(B.TT ,0) AS ThanhTienLech
		FROM
		(
			SELECT tcdt.SoHopDong,
			tcdt.HopDongID,
			tcdt.HopDongChiTietREF,
			tcdt.NgayThucHien,
			SUM(tcdt.SoLuongThucChay) AS SLChay,
			SUM(tcdt.SoLuongThucChayKM) AS SLKM,
			tcdt.DonGia,
			SUM(tcdt.ThanhTienThucChayTruocTrietKhau) AS TT
			FROM   ThucChayDaTinh tcdt
			WHERE  tcdt.DmSanPhamREF  IN 
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
							, 771, 772 ,775,792 , 805 , 806 , 817,5012
						)
			AND CONVERT(date, tcdt.NgayThucHien) BETWEEN @StartDate AND @EndDate
			GROUP BY
			tcdt.SoHopDong,
			tcdt.HopDongID,
			tcdt.HopDongChiTietREF,
			tcdt.DonGia,
			tcdt.NgayThucHien 
		)A
		FULL OUTER JOIN
		(                  
			SELECT 
			tt.ThucChayHopDongChiTietID,
			tt.HopDongREF,
			tt.HopDongChiTietREF,
			COUNT(tt.HopDongChiTietREF) AS SoLuong,
			hdct.DonGia,
			hdct.DonGia * COUNT(HopDongChiTietREF) AS TT, 
			CASE WHEN tt.CreatedAt >= tt.LastModifiedAt THEN 
				 CONVERT(date, tt.CreatedAt)
			ELSE CONVERT(date, tt.LastModifiedAt)
			END NgayThucHien 												
			FROM   ThucChayHopDongChiTiet tt LEFT JOIN HopDongChiTiet hdct 
			ON tt.HopDongChiTietREF = hdct.HopDongChiTietID 
			AND tt.HopDongREF = hdct.HopDongFK
			WHERE  hdct.DmSanPhamREF  IN 
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
						)
			and
			(
			CASE 
			WHEN tt.CreatedAt >= tt.LastModifiedAt THEN 
				 CONVERT(date, tt.CreatedAt)
			ELSE CONVERT(date, tt.LastModifiedAt)
			END
			) BETWEEN @StartDate AND @EndDate
			AND tt.HopDongChiTietREF <> 0	                          
			AND tt.DeletedStatus = 0
			GROUP BY
			tt.HopDongREF,
			tt.HopDongChiTietREF,
			hdct.DonGia,
			tt.CreatedAt,
			tt.LastModifiedAt,
			tt.ThucChayHopDongChiTietID
		)
		B ON 
		( 
			A.HopDongID = B.HopDongREF
			AND A.HopDongChiTietREF = B.HopDongChiTietREF
			AND A.NgayThucHien = B.NgayThucHien
		)
		WHERE 
		(ISNULL(A.SLChay, 0) + ISNULL(A.SLKM, 0) - ISNULL(B.SoLuong,0)) <> 0 OR 
		ISNULL(A.TT ,0) - ISNULL(B.TT ,0) <> 0
END

```
