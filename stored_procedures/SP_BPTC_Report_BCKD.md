# Stored Procedure: `BPTC_Report_BCKD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.780000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.780000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinBCKDID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Report_BCKD] ( 
	@ThongTinBCKDID INT	
)
AS 
    BEGIN
		
        DECLARE @NamBaoCao INT
        SELECT  @NamBaoCao = YEAR(ThoiGianKetThuc)
        FROM    dbo.BPTC_ThongTinBCKD
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
        
        DECLARE @DonVi INT = 1000000000 --1 TỶ
        
		--1.BPTC_ThongTinBCKD
        SELECT  BPTC_ThongTinBCKDID ,
                LoaiBaoCaoKinhDoanh ,
                TenLoaiBaoCaoKinhDoanh ,
                TenBaoCaoKinhDoanh ,
                ThoiGianBatDau ,
                ThoiGianKetThuc ,
                NguoiLap ,
                NgayLap ,
                TrangThaiPheDuyet ,
                NguoiPheDuyet ,
                NgayPheDuyet ,
                CreatedBy ,
                CreatedAt ,
                LastModifiedBy ,
                LastModifiedAt
        FROM    dbo.BPTC_ThongTinBCKD
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
        
		--2.BPTC_ThongTinBCKD_Khoi
        SELECT  ThoiGian ,
                dbo.FormatNumber(DoanhSoDanhSo) DoanhSoDanhSo ,
                dbo.FormatNumber(DoanhSoHaiDau) DoanhSoHaiDau ,
                dbo.FormatNumber(DoanhSoXuatHoaDon) DoanhSoXuatHoaDon ,
                dbo.FormatNumber(DoanhSoThucChay) DoanhSoThucChay ,
                dbo.FormatNumber(DoanhSoTienVe) DoanhSoTienVe
        FROM    dbo.BPTC_ThongTinBCKD_Khoi
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --3.BPTC_ThongTinBCKD_Khoi_Con
        SELECT  CASE ThoiGian WHEN N'Tăng trưởng' THEN N'Tăng trưởng (%)' ELSE ThoiGian END ThoiGian ,
				dbo.FormatNumber(DoanhSoDanhSo) DoanhSoDanhSo,                                
                dbo.FormatNumber(DoanhSoHaiDau) DoanhSoHaiDau ,
                dbo.FormatNumber(DoanhSoXuatHoaDon) DoanhSoXuatHoaDon ,
                dbo.FormatNumber(DoanhSoThucChay) DoanhSoThucChay ,
                dbo.FormatNumber(DoanhSoTienVe) DoanhSoTienVe
        FROM    dbo.BPTC_ThongTinBCKD_Khoi_Bro
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
		--4.BPTC_ThongTinBCKD_Khoi_DanhSo
        SELECT  BPTC_ThongTinBCKD_Khoi_DanhSoID ,
                BPTC_ThongTinBCKDREF ,
                TenBaoCaoKinhDoanh ,
                ThoiGian ,
                N'Tháng ' + ThoiGian AS ThoiGianShow ,
                ROUND(DoanhSoChiTieu / 1000000000, 0) AS DoanhSoChiTieu ,
                ROUND(DoanhSoDanhSoCungKy / 1000000000, 0) AS DoanhSoDanhSoCungKy ,
                ROUND(DoanhSoDanhSo / 1000000000, 0) AS DoanhSoDanhSo ,
                ' ' AS ItemLabel
        FROM    dbo.BPTC_ThongTinBCKD_Khoi_DanhSo
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        	
		--5.BPTC_ThongTinBCKD_Khoi_HoaDon
        SELECT  BPTC_ThongTinBCKD_Khoi_HoaDonID ,
                BPTC_ThongTinBCKDREF ,
                ThoiGian ,
                N'Tháng ' + ThoiGian AS ThoiGianShow ,
                ROUND(ChiTieuXuatHoaDon / @DonVi, 0) AS ChiTieuXuatHoaDon ,
                ROUND(DoanhSoXuatHoaDonCungKy / @DonVi, 0) AS DoanhSoXuatHoaDonCungKy ,
                ROUND(DoanhSoXuatHoaDon / @DonVi, 0) AS DoanhSoXuatHoaDon ,
                ' ' AS ItemLabel
        FROM    dbo.BPTC_ThongTinBCKD_Khoi_HoaDon
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --6.BPTC_ThongTinBCKD_Khoi_ThucChay
        SELECT  BPTC_ThongTinBCKD_Khoi_ThucChayID ,
                BPTC_ThongTinBCKDREF ,
                ThoiGian ,
                N'Tháng ' + ThoiGian AS ThoiGianShow ,
                ROUND(ChiTieuThucChay / @DonVi, 0) AS ChiTieuThucChay ,
                ROUND(DoanhSoThucChayCungKy / @DonVi, 0) AS DoanhSoThucChayCungKy ,
                ROUND(DoanhSoThucChay / @DonVi, 0) AS DoanhSoThucChay ,
                ' ' AS ItemLabel
        FROM    dbo.BPTC_ThongTinBCKD_Khoi_ThucChay
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --7.BPTC_ThongTinBCKD_BoPhan
        SELECT  TenBoPhan ,
                ISNULL(dbo.FormatNumber(ROUND(DoanhSoDanhSo, 0)), 0) AS DoanhSoDanhSo ,
                ISNULL(dbo.FormatNumber(ROUND(DoanhSoHaiDau, 0)), 0) AS DoanhSoHaiDau ,
                ISNULL(dbo.FormatNumber(ROUND(DoanhSoThucChay, 0)), 0) AS DoanhSoThucChay ,
                ISNULL(dbo.FormatNumber(ROUND(DoanhSoXuatHoaDon, 0)), 0) AS DoanhSoXuatHoaDon ,
                ISNULL(dbo.FormatNumber(ROUND(DoanhSoTienVe, 0)), 0) AS DoanhSoTienVe ,
                ' ' AS ItemLabel
        FROM    dbo.BPTC_ThongTinBCKD_BoPhan
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        ORDER BY ThuTuHienThi
        
        --8.BPTC_ThongTinBCKD_BoPhan_DanhSoHaiDau
        SELECT  TenBoPhan ,
                ROUND(DoanhSoDanhSo / @DonVi, 0) AS DoanhSoDanhSo ,
                ROUND(DoanhSoHaiDau / @DonVi, 0) AS DoanhSoHaiDau ,
                ' ' AS ItemLabel
        FROM    dbo.BPTC_ThongTinBCKD_BoPhan_DanhSoHaiDau
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        ORDER BY TenBoPhan
        
        --9.BPTC_ThongTinBCKD_SanPham
        SELECT  TenSanPham ,
                dbo.FormatNumber(DoanhSoDanhSo) DoanhSoDanhSo ,
                dbo.FormatNumber(DoanhSoHaiDau) DoanhSoHaiDau ,
                dbo.FormatNumber(DoanhSoThucChay) DoanhSoThucChay ,
                dbo.FormatNumber(ChiTieuThucChay) ChiTieuThucChay ,
                ROUND(TangTruongDoanhSo,2) AS TangTruongDoanhSo ,
                ROUND(TangTruongThucChay,2) AS TangTruongThucChay
        FROM    dbo.BPTC_ThongTinBCKD_SanPham
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --10.BPTC_ThongTinBCKD_XuatHoaDon
        SELECT  CASE WHEN CONVERT(INT, Nam_HopDong) <= 12
                     THEN 'T' + Nam_HopDong + '/'
                          + CONVERT(NVARCHAR(4), @NamBaoCao)
				     WHEN CONVERT(INT, Nam_HopDong) = 13
                     THEN N'Tổng'
                     ELSE Nam_HopDong
                END AS Nam_HopDongShow ,
                Nam_HopDong ,
                DoanhSoXuatHDNamTruoc ,
                DoanhSoXuatHD ,
                DoanhSoHaiDau ,
                GiaTriChuaXuatHD ,
                dbo.FormatNumber(DoanhSoXuatHDNamTruoc) DoanhSoXuatHDNamTruocShow ,
                dbo.FormatNumber(DoanhSoXuatHD) DoanhSoXuatHDShow ,
                dbo.FormatNumber(DoanhSoHaiDau) DoanhSoHaiDauShow ,
                dbo.FormatNumber(GiaTriChuaXuatHD) GiaTriChuaXuatHDShow ,
                ROUND(TiLeXuatHD_HD, 2) TiLeXuatHD_HD
        FROM    dbo.BPTC_ThongTinBCKD_XuatHoaDon
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --11.BPTC_ThongTinBCKD_XuatHoaDon_Nam        
        SELECT  Thang  AS Thang,
				CASE WHEN Thang > 12 THEN
					CONVERT(NVARCHAR(10),Thang)
				ELSE
					'T' + CONVERT(NVARCHAR(10), Thang) END
					ThangShow,                
                ROUND(NamBaoCaoHT_Thang1 / @DonVi, 3) NamBaoCaoHT_Thang1 ,
                ROUND(NamBaoCaoHT_Thang2 / @DonVi, 3) NamBaoCaoHT_Thang2 ,
                ROUND(NamBaoCaoHT_Thang3 / @DonVi, 3) NamBaoCaoHT_Thang3 ,
                ROUND(NamBaoCaoHT_Thang4 / @DonVi, 3) NamBaoCaoHT_Thang4 ,
                ROUND(NamBaoCaoHT_Thang5 / @DonVi, 3) NamBaoCaoHT_Thang5 ,
                ROUND(NamBaoCaoHT_Thang6 / @DonVi, 3) NamBaoCaoHT_Thang6 ,
                ROUND(NamBaoCaoHT_Thang7 / @DonVi, 3) NamBaoCaoHT_Thang7 ,
                ROUND(NamBaoCaoHT_Thang8 / @DonVi, 3) NamBaoCaoHT_Thang8 ,
                ROUND(NamBaoCaoHT_Thang9 / @DonVi, 3) NamBaoCaoHT_Thang9 ,
                ROUND(NamBaoCaoHT_Thang10 / @DonVi, 3) NamBaoCaoHT_Thang10 ,
                ROUND(NamBaoCaoHT_Thang11 / @DonVi, 3) NamBaoCaoHT_Thang11 ,
                ROUND(NamBaoCaoHT_Thang12 / @DonVi, 3) NamBaoCaoHT_Thang12 ,
                ' ' AS ItemLabel
        FROM    dbo.BPTC_ThongTinBCKD_XuatHoaDon_Nam
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --12.BPTC_ThongTinBCKD_XuatHoaDon_ThucChay
        SELECT  Thang ,
                'Tháng ' + CONVERT(NVARCHAR(10), Thang) ThangShow ,
                ROUND(DoanhSoThucChay / @DonVi, 0) DoanhSoThucChay ,
                ROUND(DoanhSoHoaDon / @DonVi, 0) DoanhSoHoaDon ,
                ' ' AS ItemLabel
        FROM    BPTC_ThongTinBCKD_XuatHoaDon_ThucChay
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID   
        
        --13.BPTC_ThongTinBCKD_Huy_ThayDoi
        SELECT  BPTC_ThongTinBCKDID ,
                HopDong_Thang ,
                CASE WHEN HopDong_Thang<=12 THEN 
                N'Tháng ' + HopDong_Thang ELSE N'Tổng' END AS HopDong_ThangShow ,
                dbo.FormatNumber(DoanhSoDanhSo) DoanhSoDanhSo ,
                dbo.FormatNumber(DoanhSoHaiDau) DoanhSoHaiDau ,
                ROUND(TiLeDanhSo_TongDanhSo, 0) TiLeDanhSo_TongDanhSo ,
                ROUND(TiLeHaiDau_TongHaiDau, 0) TiLeHaiDau_TongHaiDau
        FROM    dbo.BPTC_ThongTinBCKD_Huy_ThayDoi
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
        
        --14.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong     
        SELECT  BPTC_ThongTinBCKD_Huy_ThayDoi_HopDongID AS ID ,
                SoHopDong ,
                TenNhanVien ,
                TenPhongBan ,
                NhanHang_KhacHang ,
                dbo.FormatNumber(GiaTriHuyThayDoi) GiaTriHuyThayDoi ,
                LyDoHuy
        FROM    dbo.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --15.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong_Bro     
        SELECT  BPTC_ThongTinBCKD_Huy_ThayDoi_HopDongID AS ID ,
                SoHopDong ,
                TenNhanVien ,
                TenPhongBan ,
                NhanHang_KhacHang ,
                dbo.FormatNumber(GiaTriHuyThayDoi) GiaTriHuyThayDoi ,
                LyDoHuy
        FROM    dbo.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong_Bro
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        --16.COMMENTS
        CREATE TABLE #COMMENT
            (
              PageFooter NVARCHAR(255) ,
              PageHeader1 NVARCHAR(255) ,
              NguoiLap NVARCHAR(255) ,
              NgayBatDau DATETIME ,
              NgayKetThuc DATETIME ,
              NoiDungDanhGia_Khoi NVARCHAR(500) ,
              NoiDungDanhGia_Khoi_DanhSo NVARCHAR(500) ,
              NoiDungDanhGia_Khoi_HoaDon NVARCHAR(500) ,
              NoiDungDanhGia_Khoi_ThucChay NVARCHAR(500) ,
              NoiDungDanhGia_BoPhan NVARCHAR(500) ,
              NoiDungDanhGia_SanPham NVARCHAR(500) ,
              NoiDungDanhGia_XuatHoaDon NVARCHAR(500) ,
              NoiDungDanhGia_XuatHoaDon_Nam NVARCHAR(500) ,
              NoiDungDanhGia_XuatHoaDon_ThucChay NVARCHAR(500) ,
              NoiDungDanhGia_Huy_ThayDoi NVARCHAR(500) ,
              NoiDungDanhGia_Huy_ThayDoi_HopDong NVARCHAR(500)
            )
        
        DECLARE @PageFooter NVARCHAR(255)
        DECLARE @PageHeader1 NVARCHAR(255)
        DECLARE @NgayBatDau DATETIME
        DECLARE @NgayKetThuc DATETIME
        
        DECLARE @NoiDungDanhGia_Khoi NVARCHAR(500)
        DECLARE @NoiDungDanhGia_Khoi_DanhSo NVARCHAR(500)
        DECLARE @NoiDungDanhGia_Khoi_HoaDon NVARCHAR(500)
        DECLARE @NoiDungDanhGia_Khoi_ThucChay NVARCHAR(500)
        DECLARE @NoiDungDanhGia_BoPhan NVARCHAR(500)
        DECLARE @NoiDungDanhGia_SanPham NVARCHAR(500)
        
        DECLARE @NoiDungDanhGia_XuatHoaDon NVARCHAR(500)
        DECLARE @NoiDungDanhGia_XuatHoaDon_Nam NVARCHAR(500)
        DECLARE @NoiDungDanhGia_XuatHoaDon_ThucChay NVARCHAR(500)
        DECLARE @NoiDungDanhGia_Huy_ThayDoi NVARCHAR(500)
        DECLARE @NoiDungDanhGia_Huy_ThayDoi_HopDong NVARCHAR(500)
        
        SELECT  @NoiDungDanhGia_Khoi = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_Khoi
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_Khoi_DanhSo = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_Khoi_DanhSo
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_Khoi_HoaDon = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_Khoi_HoaDon
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
       
        SELECT  @NoiDungDanhGia_Khoi_ThucChay = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_Khoi_ThucChay
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_BoPhan = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_BoPhan
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
       
        SELECT  @NoiDungDanhGia_SanPham = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_SanPham
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_XuatHoaDon = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_XuatHoaDon
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_XuatHoaDon_Nam = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_XuatHoaDon_Nam
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_XuatHoaDon_ThucChay = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_XuatHoaDon_ThucChay
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_Huy_ThayDoi = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_Huy_ThayDoi
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
        
        SELECT  @NoiDungDanhGia_Huy_ThayDoi_HopDong = NoiDungDanhGia
        FROM    dbo.BPTC_ThongTinBCKD_Huy_ThayDoi_HopDong
        WHERE   BPTC_ThongTinBCKDREF = @ThongTinBCKDID
        
        SELECT  @PageFooter = N'# Dữ liệu cập nhật ngày '
                + CONVERT(NVARCHAR(10), NgayLap, 103) + ' (có VAT)' ,
                @PageHeader1 = N'Financial Department, '
                + CONVERT(NVARCHAR(10), NgayLap, 103) ,
                @NgayBatDau = ThoiGianBatDau ,
                @NgayKetThuc = ThoiGianKetThuc
        FROM    dbo.BPTC_ThongTinBCKD
        WHERE   BPTC_ThongTinBCKDID = @ThongTinBCKDID
        
        INSERT  INTO #COMMENT
                ( NoiDungDanhGia_Khoi ,
                  NoiDungDanhGia_Khoi_DanhSo ,
                  NoiDungDanhGia_Khoi_HoaDon ,
                  NoiDungDanhGia_Khoi_ThucChay ,
                  NoiDungDanhGia_BoPhan ,
                  NoiDungDanhGia_SanPham ,
                  PageFooter ,
                  PageHeader1 ,
                  NgayBatDau ,
                  NgayKetThuc ,
                  NoiDungDanhGia_XuatHoaDon ,
                  NoiDungDanhGia_XuatHoaDon_Nam ,
                  NoiDungDanhGia_XuatHoaDon_ThucChay ,
                  NoiDungDanhGia_Huy_ThayDoi ,
                  NoiDungDanhGia_Huy_ThayDoi_HopDong
                )
        VALUES  ( @NoiDungDanhGia_Khoi ,
                  @NoiDungDanhGia_Khoi_DanhSo ,
                  @NoiDungDanhGia_Khoi_HoaDon ,
                  @NoiDungDanhGia_Khoi_ThucChay ,
                  @NoiDungDanhGia_BoPhan ,
                  @NoiDungDanhGia_SanPham ,
                  @PageFooter ,
                  @PageHeader1 ,
                  @NgayBatDau ,
                  @NgayKetThuc ,
                  @NoiDungDanhGia_XuatHoaDon ,
                  @NoiDungDanhGia_XuatHoaDon_Nam ,
                  @NoiDungDanhGia_XuatHoaDon_ThucChay ,
                  @NoiDungDanhGia_Huy_ThayDoi ,
                  @NoiDungDanhGia_Huy_ThayDoi_HopDong
                )
        
        SELECT  *
        FROM    #COMMENT ;
        
        DROP TABLE #COMMENT
        
    END

```
